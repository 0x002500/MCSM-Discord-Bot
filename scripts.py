import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv('.env')
ADDRESS = os.getenv('MCSMANAGER_ADDRESS')
API_KEY = os.getenv('MCSMANAGER_API_KEY')

headers = {
    "X-Requested-With": "XMLHttpRequest",
    "Content-Type": "application/json; charset=UTF-8",
}


def function_statusCheck(data):
    status = data["status"]
    if status == "200":
        return True
    elif status == "400":
        return "(400) Query String Error"
    elif status == "403":
        return "(403) Permission Denied"
    elif status == "404":
        return "(404) Not Found"
    elif status == "500":
        return "(500) Internal Server Error"
    else:
        return "(Unknown) Error"


def function_getOverview():
    response = requests.get(ADDRESS + "/api/overview?apikey=" + API_KEY, headers=headers).json()
    status = function_statusCheck(response)
    if status is True:
        data_set = {
            "status": response["status"],
            "panel_version": response["data"]["version"],
            "specified_daemon_version": response["data"]["specifiedDaemonVersion"],
            "record_login": response["data"]["record"]["logined"],
            "record_illegal_access": response["data"]["record"]["illegalAccess"],
            "record_ban_ips": response["data"]["record"]["banips"],
            "record_login_failed": response["data"]["record"]["loginFailed"],
            "remote_available": response["data"]["remoteCount"]["available"],
            "remote_total": response["data"]["remoteCount"]["total"],
        }
        return data_set
    else:
        return status
