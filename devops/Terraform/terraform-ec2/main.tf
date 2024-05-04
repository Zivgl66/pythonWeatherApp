terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region  = "us-east-1"
}


module "security" {
  source = "./modules/"
}

# EC2 instance deploy
resource "aws_instance" "ubuntu_server" {
  ami           = "ami-04b70fa74e45c3917"
  instance_type = "t2.micro"
  vpc_security_group_ids = [module.security.security_groups]

    tags = {
      Name = "ziv_ubuntu"
  }
}

