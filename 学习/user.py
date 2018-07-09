# :coding: utf-8
# :copyright: Copyright (c) 2014 ftrack

import uuid

import sqlalchemy
from sqlalchemy import (
    Column, types, Boolean, Unicode, func, ForeignKey, event
)
from sqlalchemy.orm import validates, relation, backref
from sqlalchemy.ext.associationproxy import association_proxy

from . import mixin
from .appointment import Appointment
from .membership import Membership
from .hashed_property import HashedProperty
from .resource import Resource
from .component import Component

from ftserver.lib.license import License
import ftserver.lib.exceptions


class User(Resource, mixin.Tablename, mixin.TableArgs):
    '''Represent a user.'''

    userid = Column(
        types.CHAR(36), ForeignKey('resource.id'), primary_key=True
    )

    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'inherit_condition': userid == Resource.id
    }

    username = Column(
        Unicode(255), unique=True, nullable=False,
        default=lambda: u'aaa-NEWUSER' + unicode(uuid.uuid1())
    )
    isactive = Column(Boolean, nullable=False, default=False)

    #: Flag indicating a pending details update requirement.
    require_details_update = Column(Boolean, nullable=False, default=False)

    #: Flag indicating a pending password update requirement.
    require_password_update = Column(Boolean, nullable=False, default=False)

    thumbid = sqlalchemy.Column(
        sqlalchemy.CHAR(36),
        sqlalchemy.ForeignKey('component.id'),
        nullable=True
    )
    thumbnail = sqlalchemy.orm.relationship(Component)

    firstname = Column(Unicode(255), default=u'first')
    lastname = Column(Unicode(255), default=u'last')

    email = Column(Unicode(255))

    fullname = 'Name Placeholder'

    apikey = Column(types.CHAR(36), nullable=False)

    password_hash = Column(Unicode(40), nullable=False)
    password_salt = Column(Unicode(40), nullable=False)

    password = HashedProperty(
        'password_hash', 'password_salt',
        # Optional function to enable generating the hash on the db side
        dbhashfunc=(lambda pw, salt: func.sha1(pw + salt))
    )

    typeid = Column(
        types.CHAR(36), ForeignKey('user_type.typeid'),
        default='ac9fa5aa-4361-11e0-b7cc-0019bb4983d8'
    )

    type = relation('UserType', backref=backref('users'))

    tasks = relation(
        'Task', lazy='dynamic', passive_deletes=True, backref=backref(
            'users'
        ),
        primaryjoin=(
            'and_(Appointment.resource_id == User.userid,'
            'Appointment.type == "assignment")'
        ), secondaryjoin='Appointment.context_id == Task.taskid',
        secondary=Appointment.__table__,
        foreign_keys='[Appointment.resource_id, Appointment.context_id]'
    )

    # Extra eagerloaded relation between users and tasks.
    eagerTasks = relation(
        'Task', primaryjoin=(
            'and_(Appointment.resource_id == User.userid,'
            ' Appointment.type == "assignment")'
        ), secondaryjoin='Appointment.context_id == Task.taskid',
        secondary=Appointment.__table__,
        foreign_keys='[Appointment.resource_id, Appointment.context_id]',
        passive_deletes=True
    )

    groups = association_proxy(
        'user_memberships', 'membership_group',
        creator=lambda group: Membership(
            group_id=group.id
        )
    )

    def __init__(self, *args, **kw):
        '''Initialise user.'''
        super(User, self).__init__(*args, **kw)
        self.password = uuid.uuid4().hex
        self.resetApiKey()

    def __repr__(self):
        '''Return representation.'''
        return '<User("{0}")>'.format(self.userid)

    def resetApiKey(self):
        '''Reset user API key.'''
        self.apikey = str(uuid.uuid4())

    @staticmethod
    def getNameOrDefault(user):
        '''Return *user* full name or default value.'''
        return user.getName() if user else 'Unknown user'

    def getName(self):
        '''Return full name for user.'''
        return str(self.firstname) + ' ' + str(self.lastname)

    def getThumbid(self):
        '''Return thumbid or empty string.'''
        return self.thumbid if self.thumbid else ''

    @validates('isactive')
    def validate_isactive(self, key, isactive):
        '''Check license if user is being activated.'''
        if isactive is True:
            license = License()
            canEnable = license.canEnableMoreUsers()

            if not canEnable:
                return False

        return isactive

    @classmethod
    def getFields(cls):
        '''Return fields for model.'''
        secretFields = (
            'password_hash',
            'password_salt',
            'apikey',
            'require_password_update',
            'require_details_update'
        )

        fields = []
        for key in super(User, cls).getFields():
            if key not in secretFields:
                fields.append(key)

        return fields


def validateUserBeforeInsert(mapper, connection, target):
    '''Validate task before insert.'''
    if target.userid and target.id != target.entityId():
        raise ftserver.lib.exceptions.ValidationError(
            'User.userid cannot be set manually without setting Resource.id.'
        )

event.listen(
    User, 'before_insert', validateUserBeforeInsert
)
