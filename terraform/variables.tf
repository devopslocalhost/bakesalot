variable "aws_region" {
  type        = string
  description = "The region where the instance will be run on AWS"
  default     = "us-east-1"
}

variable "aws_instance_type" {
  type        = string
  description = "The instance type on aws"
  default     = "t2.micro"
}

variable "ami" {
  type        = string
  description = "AMI ID of the instance running on AWS"
  default     = "ami-08d4ac5b634553e16"
}

variable "image" {
  type        = string
  description = "Image ID the droplet running on digitalocean"
  default     = "ubuntu-18-04-x64"
}

variable "digital_region" {
  type        = string
  description = "The region where the instance will be run on digitalocean"
  default     = "nyc1"
}

variable "size" {
  type        = string
  description = "Size of the digitalocean droplet"
  default     = "s-1vcpu-1gb"
}