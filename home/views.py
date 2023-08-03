from django.shortcuts import render, redirect
from . models import Category, AiTool, Contact
from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.contrib import messages

# Create your views here.
def home(request, category_slug=None):
    category = None
    tools = None
    categories = Category.objects.all()
    selected_category = None
    tools_per_page = 5  # Show 5 tools per page

    if category_slug is not None:
        category = get_object_or_404(Category, slug=category_slug)
        selected_category = category
        tools = AiTool.objects.filter(category=category).order_by('id')
    else:
        tools = AiTool.objects.all().order_by('id')

    paginator = Paginator(tools, tools_per_page)
    page = request.GET.get('page', 1)

    try:
        paged_tools = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paged_tools = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results.
        paged_tools = paginator.page(paginator.num_pages)

    # Calculate the range of page numbers to display, with ellipsis if needed
    page_range = paginator.get_elided_page_range(paged_tools.number, on_each_side=2, on_ends=1)

    context = {
        'categories': categories,
        'selected_category': selected_category,
        'tools': paged_tools,
        'page_range': page_range,
    }
    return render(request, 'home.html', context)



def tool_detail(request, tool_slug):
    try:
        single_tool = AiTool.objects.get(slug = tool_slug)
        similar_tools = AiTool.objects.filter(category__in=single_tool.category.all()).exclude(id=single_tool.id)[:3]
        
    except:
        pass
    context = {
        'single_tool' : single_tool,
        'tools' : similar_tools,
    }
    return render(request, 'tool_description.html',context)


def search(request):
    if 'search' in request.GET:
        keyword = request.GET['search']
        if keyword:
            tools = AiTool.objects.order_by('-created_date').filter(Q(description__icontains = keyword) | Q(name__icontains = keyword))
            paginator = Paginator(tools,3)
            page = request.GET.get('page')
            if not page:
                page = 1
            paged_tools = paginator.get_page(page)
            tools_count = tools.count()
            paged_tools.adjusted_elided_pages = paginator.get_elided_page_range(page)
            
            
            all_tools = AiTool.objects.all()
            context = {
                'all_tools' : all_tools,
                'keyword' : keyword,
                'tools' : paged_tools,
                'tools_count' : tools_count,
            }
            return render(request, 'search.html', context)
    else:
        return render(request, 'search.html')
    
    
    
def contact(request):
    if request.method == 'POST':
        name    = request.POST['name']
        surname = request.POST['surname']
        email   = request.POST['email']
        phone   = request.POST['phone']
        message = request.POST['message']
        contact = Contact.objects.create(customer_name=name,customer_surname=surname, email = email,phone_number = phone, message = message)
        contact.save()
        
        messages.success(request, 'Your details have been submitted you will be contacted shortly')
        return redirect('contact')
    
    return render(request, 'contacts.html')