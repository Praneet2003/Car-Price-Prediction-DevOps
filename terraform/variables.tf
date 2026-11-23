variable "aws_region" {
  description = "AWS region where infrastructure will be deployed"
  type        = string
  default     = "ap-south-1"
}
variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"
}

variable "instance_name" {
  description = "Name of the EC2 instance"
  type        = string
  default     = "Car-Price-Prediction-Server"
}
variable "ssh_allowed_ip" {
  description = "Public IP address allowed to access EC2 through SSH"
  type        = string
}
variable "key_name" {
  description = "AWS EC2 key pair name"
  type        = string
  default     = "car-price-devops-key"
}
