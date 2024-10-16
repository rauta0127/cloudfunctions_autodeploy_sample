import os
from flask import Request
import base64
from cloudevents.http import CloudEvent
import functions_framework


# Triggered from http request
def main(request: Request) -> str:
    """HTTP Cloud Function that returns commit ID, commit time, and request data.

    Args:
        request (flask.Request): The request object.

    Returns:
        str: A message with commit ID, commit time, and request data.
    """
    commit_id = os.getenv("GIT_COMMIT_ID", "UnknownCommitID")
    commit_time = os.getenv("GIT_COMMIT_TIME", "UnknownCommitTime")
    # Get the request data
    request_data = request.get_json(silent=True) or request.data.decode()
    return f"Hello, World! (Deployed from commit: {commit_id} at {commit_time})\nYour request data: {request_data}"


# # Triggered from a message on a Cloud Pub/Sub topic.
# @functions_framework.cloud_event
# def main(cloud_event: CloudEvent) -> str:
#     # Print out the data from Pub/Sub, to prove that it worked
#     commit_id = os.getenv("GIT_COMMIT_ID", "UnknownCommitID")
#     commit_time = os.getenv("GIT_COMMIT_TIME", "UnknownCommitTime")
#     message = base64.b64decode(cloud_event.data["message"]["data"]).decode()
#     return f"Hello, World! (Deployed from commit: {commit_id} at {commit_time})\nYour Pub/Sub message: {message}"
