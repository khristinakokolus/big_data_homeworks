#!/bin/bash

docker run --rm -it --network spark-network --name spark-submit -v "$(pwd)":/opt/app bitnami/spark:3 /bin/bash