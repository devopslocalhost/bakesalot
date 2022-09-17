terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
    digitalocean = {
        source  = "digitalocean/digitalocean"
        version = "~> 2.0"
    }
  }
  backend "s3" {
    bucket = "bakesalotbucket"
    key    = "arn:aws:kms:us-east-1:200549964605:key/11759d9c-da09-43e0-95c5-5c47903735c0"
    region = "us-east-1"
  }  
}
provider "aws" {
  region = "us-east-1"
}
provider "digitalocean" {

}
resource "aws_instance" "bakesalot-aws-terra" {
  ami           = "ami-08d4ac5b634553e16"
  instance_type = "t2.micro"
  tags = {
    Name = "Bakesalot-server-1"
  }
}
resource "digitalocean_droplet" "bakesalot-do-terra" {
  image  = "ubuntu-18-04-x64"
  name   = "Bakesalot-server-2"
  region = "nyc1"
  size   = "s-1vcpu-1gb"
  ssh_keys = ["bakesalot-do-ssh"]
}
