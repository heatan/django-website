from django.shortcuts import render

from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] = "加藤"
        return ctxt

class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["num_service"] = "3939393939"
        ctxt["skills"] = [
            "Python",
            "C++",
            "JavaScript",
            "Rust",
            "Go",
        ]
        return ctxt