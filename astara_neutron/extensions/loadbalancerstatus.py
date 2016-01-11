# Copyright 2014 DreamHost, LLC
#
# Author: DreamHost, LLC
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from neutron.api import extensions

from neutron_lbaas.db.loadbalancer import models
from astara_neutron.extensions import _authzbase


class LoadbalancerstatusResource(_authzbase.ResourceDelegate):
    """This resource is intended as a private API that allows the rug to change
    a router's status (which is normally a read-only attribute)
    """
    model = models.LoadBalancer

    resource_name = 'loadbalancerstatus'
    collection_name = 'loadbalancerstatuses'

    ATTRIBUTE_MAP = {
        'tenant_id': {
            'allow_post': False,
            'allow_put': False,
            'is_visible': False
        },
        'operating_status': {
            'allow_post': False,
            'allow_put': True,
            'is_visible': True,
            'enforce_policy': True,
            'required_by_policy': True
        },
        'provisioning_status': {
            'allow_post': False,
            'allow_put': True,
            'is_visible': True,
            'enforce_policy': True,
            'required_by_policy': True
        }
    }

    def make_dict(self, loadbalancer):
        """
        Convert a loadbalancer model object to a dictionary.
        """
        return {
            'tenant_id': loadbalancer['tenant_id'],
            'operating_status': loadbalancer['operating_status'],
            'provisioning_status': loadbalancer['provisioning_status'],
        }


class Loadbalancerstatus(extensions.ExtensionDescriptor):
    """
    """
    @classmethod
    def get_name(cls):
        return "loadbalancerstatus"

    @classmethod
    def get_alias(cls):
        return "akloadbalancerstatus"

    @classmethod
    def get_description(cls):
        return "A loadbalancer-status extension"

    @classmethod
    def get_namespace(cls):
        return 'http://docs.dreamcompute.com/api/ext/v1.0'

    @classmethod
    def get_updated(cls):
        return "2015-10-09T09:14:43-05:00"

    @classmethod
    def get_resources(cls):
        return [extensions.ResourceExtension(
            'akloadbalancerstatus',
            _authzbase.create_extension(LoadbalancerstatusResource()))]
