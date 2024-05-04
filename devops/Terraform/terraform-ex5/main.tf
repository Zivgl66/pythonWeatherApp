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
module "securitygroup" {
  source  = "Shossi/securitygroup/aws"
  version = "1.0.0"
}

module "security" {
    source = "./.terraform/modules/securitygroup/security_grp/"
    ip = "10.1.10.0"
}

# EC2 instance deploy
resource "aws_instance" "ubuntu_server" {
  ami           = "ami-04b70fa74e45c3917"
  instance_type = "t2.micro"
  vpc_security_group_ids = [module.security.sec_id]

    tags = {
      Name = "ziv_ubuntu_2"
  }
}