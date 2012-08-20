# Copyright 2012 TellApart, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from gevent import monkey
monkey.patch_all()

import gevent
from tellapart.taba.client.gevent import taba_client

taba_client.Initialize('test_client1', 'http://localhost:8280/post')
taba_client.RecordValue('test_name', (100, ))
taba_client.RecordValue('test_name1', (100, ))
taba_client.RecordValue('test_name2', (100, ))
taba_client.RecordValue('test_name', (1000, ))
taba_client.RecordValue('test_name1', (1000, ))
taba_client.RecordValue('test_name2', (1000, ))

gevent.sleep(1)
taba_client.Flush()

taba_client.Initialize('test_client2', 'http://localhost:8280/post')
taba_client.RecordValue('test_name3', (100, ))
taba_client.RecordValue('test_name4', (100, ))
taba_client.RecordValue('test_name5', (100, ))
taba_client.RecordValue('test_name3', (1000, ))
taba_client.RecordValue('test_name4', (1000, ))
taba_client.RecordValue('test_name5', (1000, ))

gevent.sleep(1)
taba_client.Flush()


