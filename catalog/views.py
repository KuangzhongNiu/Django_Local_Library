from django.shortcuts import render

# Create your views here.
from .models import Book, Author, BookInstance, Genre
from django.views import generic

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    # --Challenge--
    #machine_books = Book.objects.filter(title__icontains='machine')
    #number_machine_books = machine_books.count()
    #num_genres_fiction = Genre.objects.filter(name__icontains='fiction').count()
    # --Challenge--

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    num_visits += 1
    request.session['num_visits'] = num_visits

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        # --Challenge--
        #'number_machine_books': number_machine_books,
        #'num_genres_fiction': num_genres_fiction,
        # --Challenge--
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)



class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Book

# Challenge
class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    model = Author
# Challenge

