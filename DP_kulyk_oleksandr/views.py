from django.http import HttpResponse

def project(request):
  return HttpResponse('Лабораторна робота №9')

def student(request):
  return HttpResponse('Олександр Кулик')