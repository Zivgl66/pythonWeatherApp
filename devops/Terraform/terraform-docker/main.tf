# specify docker provider:
terraform {
    required_providers {
      docker = {
        source = "kreuzwerker/docker"
        version = "3.0.2"
      }
    }
}

provider "docker" {}

# define the docker container data source
resource "docker_image" "weatherapp" {
  name         = "zivgl66/ziv-repo:weatherapp-1.151"
  keep_locally = false
}

# define the docker container resource
resource "docker_container" "app" {
  image = docker_image.weatherapp.image_id
  name  = "weatherapp"

# Expose port 5000 for Flask app
  ports {
    internal = 8005
    external = 8005
  }
}

# Terraform provisioner to wait for container to be ready

resource "null_resource" "wait_for_container" {

  depends_on = [docker_container.app]

  # Local-exec provisioner to wait for container to be ready

  provisioner "local-exec" {

    command = "sleep 10"

  }

}