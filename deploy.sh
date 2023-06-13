#!/bin/bash

# 获取脚本所在目录
script_dir=$(dirname "$(readlink -f "$0")")

# 将工作目录更改为脚本所在目录
cd "$script_dir" || exit

# 检查Git仓库是否有更新
git remote update
pwd


AWS_URl="406687643298.dkr.ecr.ap-northeast-2.amazonaws.com/quizmate-chat"
RELATEST_TIME=$(date '+%Y%m%d%H%M%S')
IMAGE_NAME=quizmate-chat:$RELATEST_TIME

aws ecr get-login-password --region ap-northeast-2 | docker login --username AWS --password-stdin 406687643298.dkr.ecr.ap-northeast-2.amazonaws.com

REMOTE_URL="${AWS_URl}:${RELATEST_TIME}"
docker build -t $IMAGE_NAME .
echo "${IMAGE_NAME}"
echo "${REMOTE_URL}"
docker tag $IMAGE_NAME $REMOTE_URL
docker push $REMOTE_URL

#docker QcChatGPTAI exist, remove it
docker rm QcChatGPTAI -f


docker run -d --name QcChatGPTAI -v /home/ec2-user/workspace/python/QcChatGPTAI/history:/app/history -v /home/ec2-user/workspace/python/QcChatGPTAI/config.json:/app/config.json -p 7869:7860 $REMOTE_URL
