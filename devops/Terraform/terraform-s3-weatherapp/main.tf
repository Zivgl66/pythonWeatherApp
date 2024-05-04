terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.18.0"
    }
  }
backend "s3" {
  bucket  = "ziv-tf-state"
  key     = "state/terraform.tfstate"
  region  = "us-east-1"
  encrypt = true
  # dynamodb_table = "tf-state"
}
}
provider "aws" {
  region = "us-east-1" # Specify the region you want to use
}


# resource "aws_instance" "ubuntu" {
#   ami           = "ami-04b70fa74e45c3917"
#   instance_type = "t2.micro"

#   tags = {
#     Name = var.instance_name
#   }
# }

resource "aws_security_group" "example" {
  name_prefix = "example"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 8005
    to_port     = 8005
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

resource "aws_instance" "ubuntu" {
  ami           = "ami-04b70fa74e45c3917" // Amazon Linux 2 AMI
  instance_type = "t2.micro"
  vpc_security_group_ids = [
    aws_security_group.example.id,
  ]
  key_name      = "weather_app_key"
  user_data = <<-EOF
              #!/bin/bash
              sudo apt-get update
              sudo apt-get install ca-certificates curl
              sudo install -m 0755 -d /etc/apt/keyrings
              sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
              sudo chmod a+r /etc/apt/keyrings/docker.asc
              echo \
              "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
              $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
              sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
              sudo apt-get update
              sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
              systemctl enable docker
              systemctl start docker
              sudo chown $USER /var/run/docker.sock
              sudo docker run zivgl66/ziv-repo:weatherapp-1.151
              EOF
}

output "public_ip" {
  value = aws_instance.ubuntu.public_ip
}