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
  region = var.aws_region
}

provider "digitalocean" {

}

resource "aws_instance" "bakesalot-aws-terra" {
  ami           = var.ami
  instance_type = var.aws_instance_type
  tags = {
    Name = "Bakesalot-server-1"
  }
}

resource "digitalocean_droplet" "bakesalot-do-terra" {
  image    = var.image
  name     = "Bakesalot-server-2"
  region   = var.digital_region
  size     = var.size
  ssh_keys = ["bakesalot-do-ssh"]
}
