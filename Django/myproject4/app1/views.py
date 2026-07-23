from django.shortcuts import render
def form(request):
    if request.method=='POST':
        fname=request.POST.get("fname")
        print(fname)
        return render(request,"app1/op.html",{"fname":fname})
    return render(request,"app1/form.html")
