# Copyright 2015 Jared Rodriguez (jared.rodriguez@rackspace.com)
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from mercury_client.base import InterfaceBase


class JobInterfaceBase(InterfaceBase):
    SERVICE_URI = 'api/rpc/jobs'


class TaskInterface(InterfaceBase):
    SERVICE_URI = 'api/rpc/tasks'


class JobQuery(JobInterfaceBase):
    def __init__(self, target, query, instruction):
        super(JobQuery, self).__init__(target)
        self.query = query
        self.instruction = instruction

        self.job_id = None
        self.response_data = None

    def post_job(self):
        _payload = {
            'query': self.query,
            'instruction': self.instruction
        }
        r = self.post(data=_payload)
        try:
            self.job_id = r['job_id']
        except KeyError:
            raise Exception('Missing job_id, data contains: {}'.format(r))

    def status(self):
        return self.get('status/{}'.format(self.job_id))

    def tasks(self):
        return self.get('tasks/{}'.format(self.job_id))


class ActiveComputers(InterfaceBase):
    SERVICE_URI = 'api/active/computers'
