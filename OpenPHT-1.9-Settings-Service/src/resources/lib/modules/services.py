################################################################################
#      This file is part of OpenELEC - http://www.openelec.tv
#      Copyright (C) 2009-2013 Stephan Raue (stephan@openelec.tv)
#      Copyright (C) 2013 Lutz Fiebach (lufie@openelec.tv)
#
#  This program is dual-licensed; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with OpenELEC; see the file COPYING.  If not, see
#  <http://www.gnu.org/licenses/>.
#
#  Alternatively, you can license this library under a commercial license,
#  please contact OpenELEC Licensing for more information.
#
#  For more information contact:
#  OpenELEC Licensing  <license@openelec.tv>  http://www.openelec.tv
################################################################################
# -*- coding: utf-8 -*-

import os
import glob


class services:

    ENABLED = False
    SAMBA_NMDB = None
    SAMBA_SMDB = None
    D_SAMBA_SECURE = None
    D_SAMBA_WORKGROUP = None
    D_SAMBA_USERNAME = None
    D_SAMBA_PASSWORD = None
    D_SAMBA_MINPROTOCOL = None
    D_SAMBA_MAXPROTOCOL = None
    D_SAMBA_AUTOSHARE = None
    KERNEL_CMD = None
    SSH_DAEMON = None
    D_SSH_DISABLE_PW_AUTH = None
    OPT_SSH_NOPASSWD = None
    AVAHI_DAEMON = None
    CRON_DAEMON = None
    LIRCD_DAEMON = None
    LIRCD_UINPUT_DAEMON = None
    menu = {'4': {
        'name': 32001,
        'menuLoader': 'load_menu',
        'listTyp': 'list',
        'InfoText': 703,
        }}

    def __init__(self, oeMain):
        try:
            oeMain.dbg_log('services::__init__', 'enter_function', 0)
            self.struct = {
                'samba': {
                    'order': 1,
                    'name': 32200,
                    'not_supported': [],
                    'settings': {
                        'samba_autostart': {
                            'order': 1,
                            'name': 32204,
                            'value': None,
                            'action': 'initialize_samba',
                            'type': 'bool',
                            'InfoText': 738,
                            },
                        'samba_workgroup': {
                            'order': 2,
                            'name': 32215,
                            'value': "WORKGROUP",
                            'action': 'initialize_samba',
                            'type': 'text',
                            'parent': {
                                'entry': 'samba_autostart',
                                'value': ['1'],
                                },
                            'InfoText': 758,
                            },
                        'samba_secure': {
                            'order': 3,
                            'name': 32202,
                            'value': None,
                            'action': 'initialize_samba',
                            'type': 'bool',
                            'parent': {
                                'entry': 'samba_autostart',
                                'value': ['1'],
                                },
                            'InfoText': 739,
                            },
                        'samba_username': {
                            'order': 4,
                            'name': 32106,
                            'value': None,
                            'action': 'initialize_samba',
                            'type': 'text',
                            'parent': {
                                'entry': 'samba_secure',
                                'value': ['1'],
                                },
                            'InfoText': 740,
                            },
                        'samba_password': {
                            'order': 5,
                            'name': 32107,
                            'value': None,
                            'action': 'initialize_samba',
                            'type': 'text',
                            'parent': {
                                'entry': 'samba_secure',
                                'value': ['1'],
                                },
                            'InfoText': 741,
                            },
                        'samba_minprotocol': {
                            'order': 6,
                            'name': 32217,
                            'value': 'SMB2',
                            'action': 'initialize_samba',
                            'type': 'multivalue',
                            'values': [
                                'SMB1',
                                'SMB2',
                                'SMB3',
                                ],
                            'parent': {
                                'entry': 'samba_autostart',
                                'value': ['1'],
                                },
                            'InfoText': 756,
                            },
                        'samba_maxprotocol': {
                            'order': 7,
                            'name': 32218,
                            'value': 'SMB3',
                            'action': 'initialize_samba',
                            'type': 'multivalue',
                            'values': [
                                'SMB1',
                                'SMB2',
                                'SMB3',
                                ],
                            'parent': {
                                'entry': 'samba_autostart',
                                'value': ['1'],
                                },
                            'InfoText': 757,
                            },
                        'samba_autoshare': {
                            'order': 8,
                            'name': 32216,
                            'value': None,
                            'action': 'initialize_samba',
                            'type': 'bool',
                            'parent': {
                                'entry': 'samba_autostart',
                                'value': ['1'],
                                },
                            'InfoText': 755,
                            },
                        },
                    },
                'ssh': {
                    'order': 2,
                    'name': 32201,
                    'not_supported': [],
                    'settings': {
                        'ssh_autostart': {
                            'order': 1,
                            'name': 32205,
                            'value': None,
                            'action': 'initialize_ssh',
                            'type': 'bool',
                            'InfoText': 742,
                            },
                        'ssh_secure': {
                            'order': 2,
                            'name': 32203,
                            'value': None,
                            'action': 'initialize_ssh',
                            'type': 'bool',
                            'parent': {
                                'entry': 'ssh_autostart',
                                'value': ['1'],
                                },
                            'InfoText': 743,
                            },
                        },
                    },
                'avahi': {
                    'order': 3,
                    'name': 32207,
                    'not_supported': [],
                    'settings': {'avahi_autostart': {
                        'order': 1,
                        'name': 32206,
                        'value': None,
                        'action': 'initialize_avahi',
                        'type': 'bool',
                        'InfoText': 744,
                        }},
                    },
                'cron': {
                    'order': 4,
                    'name': 32319,
                    'not_supported': [],
                    'settings': {'cron_autostart': {
                        'order': 1,
                        'name': 32320,
                        'value': None,
                        'action': 'initialize_cron',
                        'type': 'bool',
                        'InfoText': 745,
                        }},
                    },
                'bluez': {
                    'order': 6,
                    'name': 32331,
                    'not_supported': [],
                    'settings': {
                        'enabled': {
                            'order': 1,
                            'name': 32344,
                            'value': None,
                            'action': 'init_bluetooth',
                            'type': 'bool',
                            'InfoText': 720,
                            },
                        'obex_enabled': {
                            'order': 2,
                            'name': 32384,
                            'value': None,
                            'action': 'init_obex',
                            'type': 'bool',
                            'parent': {
                                'entry': 'enabled',
                                'value': ['1'],
                                },
                            'InfoText': 751,
                            },
                        'obex_root': {
                            'order': 3,
                            'name': 32385,
                            'value': None,
                            'action': 'init_obex',
                            'type': 'folder',
                            'parent': {
                                'entry': 'obex_enabled',
                                'value': ['1'],
                                },
                            'InfoText': 752,
                            },
                        },
                    },
                'lircd': {
                    'order': 7,
                    'name': 32391,
                    'not_supported': [],
                    'settings': {
                        'lircd_autostart': {
                            'order': 1,
                            'name': 32400,
                            'value': None,
                            'action': 'initialize_lircd',
                            'type': 'bool',
                            'InfoText': 746,
                            },
                        },
                    },
                'remotepi-board': {
                    'order': 7,
                    'name': 32392,
                    'not_supported': [],
                    'settings': {
                        'remotepi_autostart': {
                            'order': 1,
                            'name': 32393,
                            'value': None,
                            'action': 'initialize_remotepi',
                            'type': 'bool',
                            'InfoText': 32394,
                            },
                        'remotepi_version': {
                            'order': 2,
                            'name': 32395,
                            'value': None,
                            'action': 'initialize_remotepi',
                            'type': 'multivalue',
                            'parent': {
                                'entry': 'remotepi_autostart',
                                'value': ['1'],
                                },
                            'values': ['2015', '2013'],
                            'InfoText': 32396,
                            },
                        },
                    },
                'hyperion': {
                    'order': 8,
                    'name': 32397,
                    'not_supported': [],
                    'settings': {
                        'hyperion_autostart': {
                            'order': 1,
                            'name': 32398,
                            'value': None,
                            'action': 'initialize_hyperion',
                            'type': 'bool',
                            'InfoText': 32399,
                            },
                        },
                    },
                }

            self.oe = oeMain
            oeMain.dbg_log('services::__init__', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('services::__init__', 'ERROR: (%s)' % repr(e))

    def start_service(self):
        try:
            self.oe.dbg_log('services::start_service', 'enter_function', 0)
            self.load_values()
            self.initialize_samba(service=1)
            self.initialize_ssh(service=1)
            self.initialize_avahi(service=1)
            self.initialize_cron(service=1)
            self.init_bluetooth(service=1)
            self.initialize_lircd(service=1)
            self.initialize_remotepi(service=1)
            self.initialize_hyperion(service=1)
            self.oe.dbg_log('services::start_service', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('services::start_service', 'ERROR: (%s)' % repr(e))

    def stop_service(self):
        try:
            self.oe.dbg_log('services::stop_service', 'enter_function', 0)
            self.oe.dbg_log('services::stop_service', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('services::stop_service', 'ERROR: (' + repr(e) + ')')

    def do_init(self):
        try:
            self.oe.dbg_log('services::do_init', 'exit_function', 0)
            self.load_values()
            self.oe.dbg_log('services::do_init', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('services::do_init', 'ERROR: (%s)' % repr(e))

    def set_value(self, listItem):
        try:
            self.oe.dbg_log('services::set_value', 'enter_function', 0)
            self.struct[listItem.getProperty('category')]['settings'][listItem.getProperty('entry')]['value'] = listItem.getProperty('value')
            self.oe.dbg_log('services::set_value', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('services::set_value', 'ERROR: (' + repr(e) + ')')

    def load_menu(self, focusItem):
        try:
            self.oe.dbg_log('services::load_menu', 'enter_function', 0)
            self.oe.winOeMain.build_menu(self.struct)
            self.oe.dbg_log('services::load_menu', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('services::load_menu', 'ERROR: (%s)' % repr(e))

    def load_values(self):
        try:
            self.oe.dbg_log('services::load_values', 'enter_function', 0)

            # SAMBA

            if os.path.isfile(self.SAMBA_NMDB) and os.path.isfile(self.SAMBA_SMDB):
                self.struct['samba']['settings']['samba_autostart']['value'] = self.oe.get_service_state('samba')
                self.struct['samba']['settings']['samba_workgroup']['value'] = self.oe.get_service_option('samba', 'SAMBA_WORKGROUP',
                        self.D_SAMBA_WORKGROUP).replace('"', '')
                self.struct['samba']['settings']['samba_secure']['value'] = self.oe.get_service_option('samba', 'SAMBA_SECURE',
                        self.D_SAMBA_SECURE).replace('true', '1').replace('false', '0').replace('"', '')
                self.struct['samba']['settings']['samba_username']['value'] = self.oe.get_service_option('samba', 'SAMBA_USERNAME',
                        self.D_SAMBA_USERNAME).replace('"', '')
                self.struct['samba']['settings']['samba_password']['value'] = self.oe.get_service_option('samba', 'SAMBA_PASSWORD',
                        self.D_SAMBA_PASSWORD).replace('"', '')
                self.struct['samba']['settings']['samba_minprotocol']['value'] = self.oe.get_service_option('samba', 'SAMBA_MINPROTOCOL',
                        self.D_SAMBA_MINPROTOCOL).replace('"', '')
                self.struct['samba']['settings']['samba_maxprotocol']['value'] = self.oe.get_service_option('samba', 'SAMBA_MAXPROTOCOL',
                        self.D_SAMBA_MAXPROTOCOL).replace('"', '')
                self.struct['samba']['settings']['samba_autoshare']['value'] = self.oe.get_service_option('samba', 'SAMBA_AUTOSHARE',
                        self.D_SAMBA_AUTOSHARE).replace('true', '1').replace('false', '0').replace('"', '')
            else:
                self.struct['samba']['hidden'] = 'true'

            # SSH

            if os.path.isfile(self.SSH_DAEMON):
                self.struct['ssh']['settings']['ssh_autostart']['value'] = self.oe.get_service_state('sshd')
                self.struct['ssh']['settings']['ssh_secure']['value'] = self.oe.get_service_option('sshd', 'SSHD_DISABLE_PW_AUTH',
                        self.D_SSH_DISABLE_PW_AUTH).replace('true', '1').replace('false', '0').replace('"', '')

                # hide ssh settings if Kernel Parameter isset

                cmd_file = open(self.KERNEL_CMD, 'r')
                cmd_args = cmd_file.read()
                if 'ssh' in cmd_args:
                    self.struct['ssh']['settings']['ssh_autostart']['value'] = '1'
                    self.struct['ssh']['settings']['ssh_autostart']['hidden'] = 'true'
                cmd_file.close()
            else:
                self.struct['ssh']['hidden'] = 'true'

            # AVAHI

            if os.path.isfile(self.AVAHI_DAEMON):
                self.struct['avahi']['settings']['avahi_autostart']['value'] = self.oe.get_service_state('avahi')
            else:
                self.struct['avahi']['hidden'] = 'true'

            # CRON

            if os.path.isfile(self.CRON_DAEMON):
                self.struct['cron']['settings']['cron_autostart']['value'] = self.oe.get_service_state('crond')
            else:
                self.struct['cron']['hidden'] = 'true'

            # BLUEZ / OBEX

            if 'bluetooth' in self.oe.dictModules:
                if os.path.isfile(self.oe.dictModules['bluetooth'].BLUETOOTH_DAEMON):
                    self.struct['bluez']['settings']['enabled']['value'] = self.oe.get_service_state('bluez')
                    if os.path.isfile(self.oe.dictModules['bluetooth'].OBEX_DAEMON):
                        self.struct['bluez']['settings']['obex_enabled']['value'] = self.oe.get_service_state('obexd')
                        self.struct['bluez']['settings']['obex_root']['value'] = self.oe.get_service_option('obexd', 'OBEXD_ROOT',
                                self.oe.dictModules['bluetooth'].D_OBEXD_ROOT).replace('"', '')
                    else:
                        self.struct['bluez']['settings']['obex_enabled']['hidden'] = True
                        self.struct['bluez']['settings']['obex_root']['hidden'] = True
                else:
                    self.struct['bluez']['hidden'] = 'true'

            # LIRCD

            if os.path.isfile(self.LIRCD_DAEMON) and os.path.isfile(self.LIRCD_UINPUT_DAEMON):
                self.struct['lircd']['settings']['lircd_autostart']['value'] = self.oe.get_service_state('lircd')
            else:
                self.struct['lircd']['hidden'] = 'true'

            # REMOTE PI

            if os.path.isfile(self.REMOTEPI_DAEMON):
                self.struct['remotepi-board']['settings']['remotepi_autostart']['value'] = \
                    self.oe.get_service_state('remotepi-board')
                self.struct['remotepi-board']['settings']['remotepi_version']['value'] = \
                    self.oe.get_service_option('remotepi-board', 'BOARD_VERSION', self.D_REMOTEPI_VERSION).replace('"', '')
            else:
                self.struct['remotepi-board']['hidden'] = 'true'

            # HYPERION

            if os.path.isfile(self.HYPERION_DAEMON):
                self.struct['hyperion']['settings']['hyperion_autostart']['value'] = \
                    self.oe.get_service_state('hyperion')
            else:
                self.struct['hyperion']['hidden'] = 'true'

            self.oe.dbg_log('services::load_values', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('services::load_values', 'ERROR: (%s)' % repr(e))

    def initialize_samba(self, **kwargs):
        try:
            self.oe.dbg_log('services::initialize_samba', 'enter_function', 0)
            self.oe.set_busy(1)
            if 'listItem' in kwargs:
                self.set_value(kwargs['listItem'])
            options = {}
            state = 1
            if self.struct['samba']['settings']['samba_autostart']['value'] == '1':
                if 'hidden' in self.struct['samba']['settings']['samba_username']:
                    del self.struct['samba']['settings']['samba_username']['hidden']
                if 'hidden' in self.struct['samba']['settings']['samba_password']:
                    del self.struct['samba']['settings']['samba_password']['hidden']
                if self.struct['samba']['settings']['samba_secure']['value'] == '1':
                    val_secure = 'true'
                else:
                    val_secure = 'false'
                if self.struct['samba']['settings']['samba_autoshare']['value'] == '1':
                    val_autoshare = 'true'
                else:
                    val_autoshare = 'false'
                options['SAMBA_WORKGROUP'] = '"%s"' % self.struct['samba']['settings']['samba_workgroup']['value']
                options['SAMBA_SECURE'] = '"%s"' % val_secure
                options['SAMBA_AUTOSHARE'] = '"%s"' % val_autoshare
                options['SAMBA_MINPROTOCOL'] = '"%s"' % self.struct['samba']['settings']['samba_minprotocol']['value']
                options['SAMBA_MAXPROTOCOL'] = '"%s"' % self.struct['samba']['settings']['samba_maxprotocol']['value']
                options['SAMBA_USERNAME'] = '"%s"' % self.struct['samba']['settings']['samba_username']['value']
                options['SAMBA_PASSWORD'] = '"%s"' % self.struct['samba']['settings']['samba_password']['value']
            else:
                state = 0
                self.struct['samba']['settings']['samba_username']['hidden'] = True
                self.struct['samba']['settings']['samba_password']['hidden'] = True
            self.oe.set_service('samba', options, state)
            self.oe.set_busy(0)
            self.oe.dbg_log('services::initialize_samba', 'exit_function', 0)
        except Exception, e:
            self.oe.set_busy(0)
            self.oe.dbg_log('services::initialize_samba', 'ERROR: (%s)' % repr(e), 4)

    def initialize_ssh(self, **kwargs):
        try:
            self.oe.dbg_log('services::initialize_ssh', 'enter_function', 0)
            self.oe.set_busy(1)
            if 'listItem' in kwargs:
                self.set_value(kwargs['listItem'])
            state = 1
            options = {}
            if self.struct['ssh']['settings']['ssh_autostart']['value'] == '1':
                if self.struct['ssh']['settings']['ssh_secure']['value'] == '1':
                    val = 'true'
                    options['SSH_ARGS'] = '"%s"' % self.OPT_SSH_NOPASSWD
                else:
                    val = 'false'
                    options['SSH_ARGS'] = '""'
                options['SSHD_DISABLE_PW_AUTH'] = '"%s"' % val
            else:
                state = 0
            self.oe.set_service('sshd', options, state)
            self.oe.set_busy(0)
            self.oe.dbg_log('services::initialize_ssh', 'exit_function', 0)
        except Exception, e:
            self.oe.set_busy(0)
            self.oe.dbg_log('services::initialize_ssh', 'ERROR: (%s)' % repr(e), 4)

    def initialize_avahi(self, **kwargs):
        try:
            self.oe.dbg_log('services::initialize_avahi', 'enter_function', 0)
            self.oe.set_busy(1)
            if 'listItem' in kwargs:
                self.set_value(kwargs['listItem'])
            state = 1
            options = {}
            if self.struct['avahi']['settings']['avahi_autostart']['value'] != '1':
                state = 0
            self.oe.set_service('avahi', options, state)
            self.oe.set_busy(0)
            self.oe.dbg_log('services::initialize_avahi', 'exit_function', 0)
        except Exception, e:
            self.oe.set_busy(0)
            self.oe.dbg_log('services::initialize_avahi', 'ERROR: (%s)' % repr(e), 4)

    def initialize_cron(self, **kwargs):
        try:
            self.oe.dbg_log('services::initialize_cron', 'enter_function', 0)
            self.oe.set_busy(1)
            if 'listItem' in kwargs:
                self.set_value(kwargs['listItem'])
            state = 1
            options = {}
            if self.struct['cron']['settings']['cron_autostart']['value'] != '1':
                state = 0
            self.oe.set_service('crond', options, state)
            self.oe.set_busy(0)
            self.oe.dbg_log('services::initialize_cron', 'exit_function', 0)
        except Exception, e:
            self.oe.set_busy(0)
            self.oe.dbg_log('services::initialize_cron', 'ERROR: (%s)' % repr(e), 4)

    def init_bluetooth(self, **kwargs):
        try:
            self.oe.dbg_log('services::init_bluetooth', 'enter_function', 0)
            self.oe.set_busy(1)
            if 'listItem' in kwargs:
                self.set_value(kwargs['listItem'])
            state = 1
            options = {}
            if self.struct['bluez']['settings']['enabled']['value'] != '1':
                state = 0
                self.struct['bluez']['settings']['obex_enabled']['hidden'] = True
                self.struct['bluez']['settings']['obex_root']['hidden'] = True
            else:
                if 'hidden' in self.struct['bluez']['settings']['obex_enabled']:
                    del self.struct['bluez']['settings']['obex_enabled']['hidden']
                if 'hidden' in self.struct['bluez']['settings']['obex_root']:
                    del self.struct['bluez']['settings']['obex_root']['hidden']
            self.oe.set_service('bluez', options, state)
            self.oe.set_busy(0)
            self.oe.dbg_log('services::init_bluetooth', 'exit_function', 0)
        except Exception, e:
            self.oe.set_busy(0)
            self.oe.dbg_log('services::init_bluetooth', 'ERROR: (' + repr(e) + ')', 4)

    def init_obex(self, **kwargs):
        try:
            self.oe.dbg_log('services::init_obex', 'enter_function', 0)
            self.oe.set_busy(1)
            if 'listItem' in kwargs:
                self.set_value(kwargs['listItem'])
            state = 1
            options = {}
            if self.struct['bluez']['settings']['obex_enabled']['value'] == '1':
                options['OBEXD_ROOT'] = '"%s"' % self.struct['bluez']['settings']['obex_root']['value']
            else:
                state = 0
            self.oe.set_service('obexd', options, state)
            self.oe.set_busy(0)
            self.oe.dbg_log('services::init_obex', 'exit_function', 0)
        except Exception, e:
            self.oe.set_busy(0)
            self.oe.dbg_log('services::init_obex', 'ERROR: (' + repr(e) + ')', 4)

    def initialize_lircd(self, **kwargs):
        try:
            self.oe.dbg_log('services::inititialize_lircd', 'enter_function', 0)
            self.oe.set_busy(1)
            if 'listItem' in kwargs:
                self.set_value(kwargs['listItem'])
            state = 1
            options = {}
            if self.struct['lircd']['settings']['lircd_autostart']['value'] != '1':
                state = 0
            self.oe.set_service('lircd', options, state)
            self.oe.set_busy(0)
            self.oe.dbg_log('services::inititialize_lircd', 'exit_function', 0)
        except Exception, e:
            self.oe.set_busy(0)
            self.oe.dbg_log('services::inititialize_lircd', 'ERROR: (' + repr(e) + ')', 4)

    def initialize_remotepi(self, **kwargs):
        try:
            self.oe.dbg_log('services::initialize_remotepi', 'enter_function', 0)
            self.oe.set_busy(1)
            if 'listItem' in kwargs:
                self.set_value(kwargs['listItem'])
            state = 1
            options = {}
            if self.struct['remotepi-board']['settings']['remotepi_autostart']['value'] != '1':
                state = 0
            if not self.struct['remotepi-board']['settings']['remotepi_version']['value'] is None and state == 1:
                options['BOARD_VERSION'] = '"%s"' % self.struct['remotepi-board']['settings']['remotepi_version']['value']
            self.oe.set_service('remotepi-board', options, state)
            self.oe.set_busy(0)
            self.oe.dbg_log('services::initialize_remotepi', 'exit_function', 0)
        except Exception, e:
            self.oe.set_busy(0)
            self.oe.dbg_log('services::initialize_remotepi', 'ERROR: (%s)' % repr(e), 4)

    def initialize_hyperion(self, **kwargs):
        try:
            self.oe.dbg_log('services::initialize_hyperion', 'enter_function', 0)
            self.oe.set_busy(1)
            if 'listItem' in kwargs:
                self.set_value(kwargs['listItem'])
            state = 1
            options = {}
            if self.struct['hyperion']['settings']['hyperion_autostart']['value'] != '1':
                state = 0
            self.oe.set_service('hyperion', options, state)
            self.oe.set_busy(0)
            self.oe.dbg_log('services::initialize_hyperion', 'exit_function', 0)
        except Exception, e:
            self.oe.set_busy(0)
            self.oe.dbg_log('services::initialize_hyperion', 'ERROR: (%s)' % repr(e), 4)

    def exit(self):
        try:
            self.oe.dbg_log('services::exit', 'enter_function', 0)
            self.oe.dbg_log('services::exit', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('services::exit', 'ERROR: (%s)' % repr(e), 4)

    def do_wizard(self):
        try:
            self.oe.dbg_log('services::do_wizard', 'enter_function', 0)
            self.oe.winOeMain.set_wizard_title(self.oe._(32311))

            # Enable ssh
            self.struct['ssh']['settings']['ssh_autostart']['value'] = '1'
            self.initialize_ssh()

            # Enable samba
            self.struct['samba']['settings']['samba_autostart']['value'] = '1'
            self.initialize_samba()

            if hasattr(self, 'samba'):
                self.oe.winOeMain.set_wizard_text(self.oe._(32313) + '[CR][CR]' + self.oe._(32312))
            else:
                self.oe.winOeMain.set_wizard_text(self.oe._(32312))
            self.oe.winOeMain.set_wizard_button_title(self.oe._(32316))
            self.set_wizard_buttons()
            self.oe.dbg_log('services::do_wizard', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('services::do_wizard', 'ERROR: (%s)' % repr(e))

    def set_wizard_buttons(self):
        try:
            self.oe.dbg_log('services::set_wizard_buttons', 'enter_function', 0)
            if self.struct['ssh']['settings']['ssh_autostart']['value'] == '1':
                self.oe.winOeMain.set_wizard_radiobutton_1(self.oe._(32201), self, 'wizard_set_ssh', True)
            else:
                self.oe.winOeMain.set_wizard_radiobutton_1(self.oe._(32201), self, 'wizard_set_ssh')
            if not 'hidden' in self.struct['samba']:
                if self.struct['samba']['settings']['samba_autostart']['value'] == '1':
                    self.oe.winOeMain.set_wizard_radiobutton_2(self.oe._(32200), self, 'wizard_set_samba', True)
                else:
                    self.oe.winOeMain.set_wizard_radiobutton_2(self.oe._(32200), self, 'wizard_set_samba')
            self.oe.dbg_log('services::set_wizard_buttons', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('services::set_wizard_buttons', 'ERROR: (%s)' % repr(e))

    def wizard_set_ssh(self):
        try:
            self.oe.dbg_log('services::wizard_set_ssh', 'enter_function', 0)
            if self.struct['ssh']['settings']['ssh_autostart']['value'] == '1':
                self.struct['ssh']['settings']['ssh_autostart']['value'] = '0'
            else:
                self.struct['ssh']['settings']['ssh_autostart']['value'] = '1'

            # ssh button does nothing if Kernel Parameter isset

            cmd_file = open(self.KERNEL_CMD, 'r')
            cmd_args = cmd_file.read()
            if 'ssh' in cmd_args:
                self.oe.notify('ssh', 'ssh enabled as boot parameter. can not disable')
            cmd_file.close()
            self.initialize_ssh()
            self.load_values()
            self.set_wizard_buttons()
            self.oe.dbg_log('services::wizard_set_ssh', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('services::wizard_set_ssh', 'ERROR: (%s)' % repr(e))

    def wizard_set_samba(self):
        try:
            self.oe.dbg_log('services::wizard_set_samba', 'enter_function', 0)
            if self.struct['samba']['settings']['samba_autostart']['value'] == '1':
                self.struct['samba']['settings']['samba_autostart']['value'] = '0'
            else:
                self.struct['samba']['settings']['samba_autostart']['value'] = '1'
            self.initialize_samba()
            self.load_values()
            self.set_wizard_buttons()
            self.oe.dbg_log('services::wizard_set_samba', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('services::wizard_set_samba', 'ERROR: (%s)' % repr(e))


