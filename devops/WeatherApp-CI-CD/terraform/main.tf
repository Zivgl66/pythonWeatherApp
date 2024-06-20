  terraform {
    required_providers {
      aws = {
        source  = "hashicorp/aws"
        version = "~> 4.0"
      }

    }
    backend "s3" {
      bucket = "ziv-tf-state"
      key    = "my-terraform-project"
      region = "us-east-1"
    }
    required_version = ">= 1.2.0"
  }

  #Adding Provider details
  provider "aws" {
    region = "us-east-1"
  }

# Create a custom VPC
resource "aws_vpc" "myvpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    "Name" = "MyProjectVPC"
  }
}

# Create Subnets
resource "aws_subnet" "Mysubnet01" {
  vpc_id                  = aws_vpc.myvpc.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "us-east-1a"
  tags = {
    "Name" = "MyPrivateSubnet01"
    "kubernetes.io/role/internal-elb" = 1
  }
}

resource "aws_subnet" "Mysubnet02" {
  vpc_id                  = aws_vpc.myvpc.id
  cidr_block              = "10.0.2.0/24"
  availability_zone       = "us-east-1b"
  tags = {
    "Name" = "MyPrivateSubnet02"
    "kubernetes.io/role/internal-elb" = 1

  }
}

resource "aws_subnet" "Mysubnet03" {
  vpc_id                  = aws_vpc.myvpc.id
  cidr_block              = "10.0.3.0/24"
  availability_zone       = "us-east-1c"
  map_public_ip_on_launch = true
  tags = {
    "Name" = "MyPublicSubnet03"
    "kubernetes.io/role/elb" = 1
  }
}

resource "aws_subnet" "Mysubnet04" {
  vpc_id                  = aws_vpc.myvpc.id
  cidr_block              = "10.0.4.0/24"
  availability_zone       = "us-east-1d"
  map_public_ip_on_launch = true
  tags = {
    "Name" = "MyPublicSubnet04"
    "kubernetes.io/role/elb" = 1
  }
}


# Create Elastic IPs for NAT Gateways
resource "aws_eip" "nat_az1" {
  vpc = true
}

resource "aws_eip" "nat_az2" {
  vpc = true
}

# Create NAT Gateways
resource "aws_nat_gateway" "nat_az1" {
  allocation_id = aws_eip.nat_az1.id
  subnet_id     = aws_subnet.Mysubnet03.id
  tags = {
    Name = "nat-gateway-az1"
  }
}

resource "aws_nat_gateway" "nat_az2" {
  allocation_id = aws_eip.nat_az2.id
  subnet_id     = aws_subnet.Mysubnet04.id
  tags = {
    Name = "nat-gateway-az2"
  }
}

# Create Internet Gateway
resource "aws_internet_gateway" "myigw" {
  vpc_id = aws_vpc.myvpc.id
  tags = {
    "Name" = "MyIGW"
  }
}

# Create Route Table for Public Subnet
resource "aws_route_table" "myroutetable01" {
  vpc_id = aws_vpc.myvpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.myigw.id
  }
  tags = {
    "Name" = "MyPublicRouteTable01"
  }
}

# Create Route Table for Public Subnet
resource "aws_route_table" "myroutetable02" {
  vpc_id = aws_vpc.myvpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.myigw.id
  }
  tags = {
    "Name" = "MyPublicRouteTable02"
  }
}

resource "aws_route_table_association" "public02" {
  subnet_id      = aws_subnet.Mysubnet04.id
  route_table_id = aws_route_table.myroutetable02.id
}


resource "aws_route_table_association" "public01" {
  subnet_id      = aws_subnet.Mysubnet03.id
  route_table_id = aws_route_table.myroutetable01.id
}

# Create Route Tables for Private Subnets
resource "aws_route_table" "private_az1" {
  vpc_id = aws_vpc.myvpc.id

  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.nat_az1.id
  }

  tags = {
    Name = "private-route-table-az1"
  }
}

resource "aws_route_table" "private_az2" {
  vpc_id = aws_vpc.myvpc.id

  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.nat_az2.id
  }

  tags = {
    Name = "private-route-table-az2"
  }
}

# Associate Private Subnets with Route Tables
resource "aws_route_table_association" "private_a" {
  subnet_id      = aws_subnet.Mysubnet01.id
  route_table_id = aws_route_table.private_az1.id
}

resource "aws_route_table_association" "private_b" {
  subnet_id      = aws_subnet.Mysubnet02.id
  route_table_id = aws_route_table.private_az2.id
}
  #Adding security group
  resource "aws_security_group" "allow_tls" {
    name_prefix = "allow_tls_"
    description = "Allow TLS inbound traffic"
    vpc_id      = aws_vpc.myvpc.id

    ingress {
      description = "ssh from VPC"
      from_port   = 22
      to_port     = 22
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }

    ingress {
      description = "http from VPC"
      from_port   = 80
      to_port     = 80
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }


    egress {
      from_port   = 0
      to_port     = 0
      protocol    = "-1"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }

  #Creating IAM role for EKS
  resource "aws_iam_role" "master" {
    name = "ed-eks-master"

    assume_role_policy = jsonencode({
      "Version" : "2012-10-17",
      "Statement" : [
        {
          "Effect" : "Allow",
          "Principal" : {
            "Service" : "eks.amazonaws.com"
          },
          "Action" : "sts:AssumeRole"
        }
      ]
    })
  }

  resource "aws_iam_role_policy_attachment" "AmazonEKSClusterPolicy" {
    policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
    role       = aws_iam_role.master.name
  }

  resource "aws_iam_role_policy_attachment" "AmazonEKSServicePolicy" {
    policy_arn = "arn:aws:iam::aws:policy/AmazonEKSServicePolicy"
    role       = aws_iam_role.master.name
  }

  resource "aws_iam_role_policy_attachment" "AmazonEKSVPCResourceController" {
    policy_arn = "arn:aws:iam::aws:policy/AmazonEKSVPCResourceController"
    role       = aws_iam_role.master.name
  }

  resource "aws_iam_role" "worker" {
    name = "ed-eks-worker"

    assume_role_policy = jsonencode({
      "Version" : "2012-10-17",
      "Statement" : [
        {
          "Effect" : "Allow",
          "Principal" : {
            "Service" : "ec2.amazonaws.com"
          },
          "Action" : "sts:AssumeRole"
        }
      ]
    })
  }

  resource "aws_iam_policy" "autoscaler" {
    name = "ed-eks-autoscaler-policy"
    policy = jsonencode({
      "Version" : "2012-10-17",
      "Statement" : [
        {
          "Action" : [
            "autoscaling:DescribeAutoScalingGroups",
            "autoscaling:DescribeAutoScalingInstances",
            "autoscaling:DescribeTags",
            "autoscaling:DescribeLaunchConfigurations",
            "autoscaling:SetDesiredCapacity",
            "autoscaling:TerminateInstanceInAutoScalingGroup",
            "ec2:DescribeLaunchTemplateVersions"
          ],
          "Effect" : "Allow",
          "Resource" : "*"
        }
      ]
    })
  }

  resource "aws_iam_role_policy_attachment" "AmazonEKSWorkerNodePolicy" {
    policy_arn = "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy"
    role       = aws_iam_role.worker.name
  }

  resource "aws_iam_role_policy_attachment" "AmazonEKS_CNI_Policy" {
    policy_arn = "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy"
    role       = aws_iam_role.worker.name
  }

  resource "aws_iam_role_policy_attachment" "AmazonSSMManagedInstanceCore" {
    policy_arn = "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
    role       = aws_iam_role.worker.name
  }

  resource "aws_iam_role_policy_attachment" "AmazonEC2ContainerRegistryReadOnly" {
    policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
    role       = aws_iam_role.worker.name
  }

  resource "aws_iam_role_policy_attachment" "x-ray" {
    policy_arn = "arn:aws:iam::aws:policy/AWSXRayDaemonWriteAccess"
    role       = aws_iam_role.worker.name
  }


  resource "aws_iam_role_policy_attachment" "s3" {
    policy_arn = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
    role       = aws_iam_role.worker.name
  }

  resource "aws_iam_role_policy_attachment" "autoscaler" {
    policy_arn = aws_iam_policy.autoscaler.arn
    role       = aws_iam_role.worker.name
  }

  data "aws_iam_instance_profile" "worker" {
    name = "ed-eks-worker-new-profile"
  }

  resource "aws_iam_instance_profile" "worker" {
    count = length(data.aws_iam_instance_profile.worker) == 0 ? 1 : 0
    name = "ed-eks-worker-new-profile"
    role = aws_iam_role.worker.name
  }

  #Creating EKS Cluster
  resource "aws_eks_cluster" "eks" {
    name     = "pc-eks"
    role_arn = aws_iam_role.master.arn

    vpc_config {
      subnet_ids = [aws_subnet.Mysubnet01.id, aws_subnet.Mysubnet02.id]
    }

    tags = {
      "Name" = "MyEKS"
    }

    depends_on = [
      aws_iam_role_policy_attachment.AmazonEKSClusterPolicy,
      aws_iam_role_policy_attachment.AmazonEKSServicePolicy,
      aws_iam_role_policy_attachment.AmazonEKSVPCResourceController,
    ]
  }

  resource "aws_instance" "kubectl-server" {
    ami                         = "ami-04b70fa74e45c3917"
    key_name                    = "weather_app_key" 
    instance_type               = "t2.micro"
    associate_public_ip_address = false
    subnet_id                   = aws_subnet.Mysubnet01.id
    vpc_security_group_ids      = [aws_security_group.allow_tls.id]

    tags = {
      Name = "kubectl"
    }
  }

  resource "aws_eks_node_group" "node-grp" {
  cluster_name    = aws_eks_cluster.eks.name
  node_group_name = "pc-node-group"
  node_role_arn   = aws_iam_role.worker.arn
  subnet_ids      = [aws_subnet.Mysubnet01.id, aws_subnet.Mysubnet02.id] # Only private subnets
  capacity_type   = "ON_DEMAND"
  disk_size       = 20
  instance_types  = ["t2.small"]

  remote_access {
    ec2_ssh_key               = "weather_app_key"
    source_security_group_ids = [aws_security_group.allow_tls.id] # Make sure this allows SSH from your IP or bastion host
  }

  labels = {
    env = "dev"
  }
  tags = {
    Name = "kube-node"
  }
  scaling_config {
    desired_size = 2
    max_size     = 3
    min_size     = 1
  }

  update_config {
    max_unavailable = 1
  }

  depends_on = [
    aws_iam_role_policy_attachment.AmazonEKSWorkerNodePolicy,
    aws_iam_role_policy_attachment.AmazonEKS_CNI_Policy,
    aws_iam_role_policy_attachment.AmazonEC2ContainerRegistryReadOnly,
  ]
}

  # # Creaton of ELB
  # resource "aws_lb" "external-alb" {
  #   name               = "External-LB"
  #   internal           = false
  #   load_balancer_type = "application"
  #   security_groups    = [aws_security_group.allow_tls.id]
  #   subnets            = [aws_subnet.Mysubnet01.id, aws_subnet.Mysubnet02.id]
  # }
  # resource "aws_lb_target_group" "target_elb" {
  #   name     = "ALB-TG"
  #   port     = 80
  #   protocol = "HTTP"
  #   vpc_id   = aws_vpc.myvpc.id
  #   health_check {
  #     path     = "/health"
  #     port     = 80
  #     protocol = "HTTP"
  #   }
  # }
  # # resource "aws_lb_target_group_attachment" "ecomm" {
  # #   target_group_arn = aws_lb_target_group.target_elb.arn
  # #   target_id        = aws_instance.ecomm.id
  # #   port             = 80
  # #   depends_on = [
  # #     aws_lb_target_group.target_elb,
  # #     aws_instance.ecomm,
  # #   ]
  # # }
  # # resource "aws_lb_target_group_attachment" "food" {
  # #   target_group_arn = aws_lb_target_group.target_elb.arn
  # #   target_id        = aws_instance.food.id
  # #   port             = 80
  # #   depends_on = [
  # #     aws_lb_target_group.target_elb,
  # #     aws_instance.food,
  # #   ]
  # # }
  # resource "aws_lb_listener" "listener_elb" {
  #   load_balancer_arn = aws_lb.external-alb.arn
  #   port              = 80
  #   protocol          = "HTTP"
  #   default_action {
  #     type             = "forward"
  #     target_group_arn = aws_lb_target_group.target_elb.arn
  #   }
  # }

