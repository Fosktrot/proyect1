from cgitb import html
from fileinput import close
from pydoc import doc
from re import template
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, context
from django.template import loader
import datetime
