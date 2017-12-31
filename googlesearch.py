# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__author__ = 'rako'

from googleapiclient.discovery import build

my_cse_id = "SEARCH_ENGINE_ID"
dev_key = "GOOGLE_CLOUD_API_KEY"

def google_search(search_term, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=dev_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

results = google_search('Tomato', my_cse_id, num=15, cr="countryIN", lr="lang_en")
for result in results:
    print(result.get('title'))
    print(result.get('link'))
    print(result.get('snippet'))
    print('\n')
