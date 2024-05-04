output "vpc_id" {
  value = aws_vpc.vpc.id
}

output "private_sub_id" {
  value = aws_subnet.public.id
}

output "public_sub_id" {
  value = aws_subnet.private.id
}
