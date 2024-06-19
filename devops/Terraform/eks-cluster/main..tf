# Provider configuration
provider "aws" {
  region = "us-east-1"  # Replace with your preferred region
}

# Optionally, if you want to organize resources with modules, you can define them here
# module "eks" {
#   source = "./eks-module"
#   # Pass necessary variables to the module
# }

# If not using modules, this file just serves as a placeholder for provider config.