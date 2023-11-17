from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class Metadata(BaseModel):
    parentResourceId:str

class LogItem(BaseModel):
    level: str
    message: str
    resourceId: str
    timestamp: datetime
    traceId: str
    spanId: str
    commit: str
    metadata: Metadata

# # Sample JSON data
# json_data = '''
# {
# 	"level": "error",
# 	"message": "Failed to connect to DB",
#     "resourceId": "server-1234",
# 	"timestamp": "2023-09-15T08:00:00Z",
# 	"traceId": "abc-xyz-123",
#     "spanId": "span-456",
#     "commit": "5e5342f",
#     "metadata": {
#         "parentResourceId": "server-0987"
#     }
# }
# '''

# # Parse JSON data using the LogItem model
# log_item = LogItem.parse_raw(json_data)

# # Access individual attributes
# print(log_item.level)
# print(log_item.timestamp)
# print(log_item.metadata.parentResourceId)