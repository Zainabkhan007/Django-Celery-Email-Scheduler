from .forms import ReviewForm
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.urls import reverse


class SendReview(TemplateView):
    template_name = 'send.html'

class EmailReview(FormView):
    template_name ="reviews.html"
    form_class=ReviewForm
    def form_valid(self,form):
        form.send_email()
        # msg="Thanks for the review"
        
        # return HttpResponse(msg)
        return HttpResponseRedirect(reverse("send"))
