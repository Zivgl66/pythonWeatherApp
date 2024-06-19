#!/bin/bash

set -e

# Variables
CLUSTER_NAME="pc-eks"
REGION="us-east-1"
VPC_ID="vpc-0fffb7a2acfd28cb3"
OIDC_PROVIDER_URL=$(aws eks describe-cluster --name $CLUSTER_NAME --region $REGION --query "cluster.identity.oidc.issuer" --output text)
SERVICE_ACCOUNT_NAMESPACE="kube-system"
SERVICE_ACCOUNT_NAME="aws-load-balancer-controller"
POLICY_NAME="AWSLoadBalancerControllerIAMPolicy"
POLICY_ARN="arn:aws:iam::aws:policy/$POLICY_NAME"

# 1. Associate IAM OIDC provider
echo "Associating IAM OIDC provider with EKS cluster..."
eksctl utils associate-iam-oidc-provider --region $REGION --cluster $CLUSTER_NAME --approve


# 4. Create a service account
echo "Creating service account..."
eksctl create iamserviceaccount \
  --cluster $CLUSTER_NAME \
  --namespace $SERVICE_ACCOUNT_NAMESPACE \
  --name $SERVICE_ACCOUNT_NAME \
  --attach-policy-arn $POLICY_ARN \
  --approve

# 5. Install the TargetGroupBinding CRDs
echo "Installing TargetGroupBinding CRDs..."
kubectl apply -k "github.com/aws/eks-charts/stable/aws-load-balancer-controller//crds?ref=master"

# 6. Add the Helm repository
echo "Adding Helm repository..."
helm repo add eks https://aws.github.io/eks-charts
helm repo update

# 7. Install the AWS Load Balancer Controller using Helm
echo "Installing AWS Load Balancer Controller using Helm..."
helm upgrade -i aws-load-balancer-controller eks/aws-load-balancer-controller \
  --set clusterName=$CLUSTER_NAME \
  --set serviceAccount.create=false \
  --set region=$REGION \
  --set vpcId=$VPC_ID \
  --set serviceAccount.name=$SERVICE_ACCOUNT_NAME \
  --namespace $SERVICE_ACCOUNT_NAMESPACE

# 8. Verify the installation
echo "Verifying installation..."
kubectl get deployment -n $SERVICE_ACCOUNT_NAMESPACE aws-load-balancer-controller

echo "AWS Load Balancer Controller installation completed successfully!"
