# Percepthor Query Service

### Development
```
sudo docker run \
  -it \
  --name service --rm \
  -p 5000:5000 --net percepthor \
  -v /home/ermiry/Documents/Work/query-service:/home/service \
  -e RUNTIME=development \
  -e PORT=5000 \
  -e CERVER_RECEIVE_BUFFER_SIZE=4096 -e CERVER_TH_THREADS=4 \
  -e CERVER_CONNECTION_QUEUE=4 \
  itpercepthor/query-service:development /bin/bash
```

## Routes

### Main

#### GET /api/service
**Access:** Public \
**Description:** Service top level route \
**Returns:**
  - 200 on success

#### GET /api/service/version
**Access:** Public \
**Description:** Returns service current version \
**Returns:**
  - 200 and version's json on success
