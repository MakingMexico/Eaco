from django.shortcuts import redirect
from django.views.generic.edit import CreateView, FormView
from cuentas.models import Usuarios, Dispositivos, Alarma
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout
from cuentas.Forms import RegisterForm
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.base import RedirectView

class LoginDir(SuccessMessageMixin, FormView):
    form_class = AuthenticationForm
    template_name = "index.html"
    success_url = reverse_lazy("cuenta:user")
    success_message = "Welcome back %(username)s!"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            print(True)
            return redirect(self.get_success_url())
        else:
            print(False)
            return super(LoginDir, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginDir, self).form_valid(form)

class Sesion(ListView):
    model = Alarma
    template_name = "user.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        self.queryset = Alarma.objects.filter(owner=Dispositivos.objects.get(id=1))
        return super(Sesion, self).dispatch(self.request, *args, **kwargs)

class Registro(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name = "registrer.html"
    success_url = reverse_lazy("cuenta:login")
    success_message = "User was created successfully"

class geta(CreateView):
    model = Alarma
    fields = ['hora']
    print("hola mundo")

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(geta, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = request.POST['fecha']
        Alarma.objects.create(owner=Dispositivos.objects.get(id=1), hora=data)

class Logout(RedirectView):
    pattern_name = 'cuenta:login'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(Logout, self).get(request, *args, **kwargs)
