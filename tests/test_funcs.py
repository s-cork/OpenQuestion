import os
import threading
import time
from server_code.server_surveys import *
import anvil.server
import pytest


@pytest.fixture(scope="session", autouse=True)
def start_up_and_tear_down():

  """
  Everything before "yield" is run before any tests
  Everything after "yield" is run after all tests have finished
  """

  # kill process on port in case it is running
  os.system("fuser -k 3030/tcp")

  # func to call app server
  def start_server():
    os.system("anvil-app-server --app ../OpenQuestion --uplink-key 42 --port 3030")

  # start app server on a thread, allowing the rest of the script to run
  threading.Thread(target=start_server).start()

  # give time for the web server to spin up before continuing
  time.sleep(60)

  # connect
  anvil.server.connect('42', url="ws://localhost:3030/_/uplink")

  yield True

  # disconnect from uplink
  anvil.server.disconnect()

  # kill process on that port
  os.system("fuser -k 3030/tcp")

# basic survey
schema={
  "title": "simple survey",
  "settings": {
  "survey_color": "#2196F3",
  "thank_you_msg": "#Thank you!"
  },
  "num_widgets": 2,
  "widgets": [
    {
      "id": 0,
      "type": "section",
      "logic": None,
      "title": "section",
      "widgets": [
        {
          "id": 1,
          "type": "text_box",
          "logic": None,
          "title": "what's your name?",
          "number": False,
          "mandatory": True,
          "placeholder": "placeholder here"
        }
      ]
    }
  ]
}

def test_save_schema():

  # current number of surveys
  cur_num_forms=len(app_tables.forms.search())

  # add a survey to the database
  save_schema(None, schema)

  # a simple assertion that there is one more survey in the database
  assert cur_num_forms < len(app_tables.forms.search())

