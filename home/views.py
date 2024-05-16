from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import courses,userinput
from RandR.models import RatingReview
from django.db.models import Avg,Count, Subquery,OuterRef  # Add this import statement
from django.db.models import Count,F
from decimal import Decimal
def home(request):
    if request.method == 'POST':
        percentage = request.POST.get('percentage')
        stream = request.POST.get('stream')
        budget = request.POST.get('budget')
        # Check if any field is missing or in incorrect format
        if not (percentage and stream and budget):
            return render(request, 'home.html', {'message': 'One or more form fields are missing or in incorrect format'})

        percentage = int(percentage)
        budget = int(budget)

        filtered_courses = courses.objects.filter(
            c_eligibility__lte=percentage,
            c_rstream=stream,
            c_tfees__lte=budget
        )
        print(filtered_courses.query)
        request.session['filtered_courses'] = list(filtered_courses.values())

        return redirect('home:transfer_courses')
    else:

        # Fetch all courses from the database
        # Fetch all courses from the database
        all_courses = courses.objects.all()

        # Calculate average rating and count of ratings for each course
        courses_with_avg_rating = []
        for course in all_courses:
            avg_rating = RatingReview.objects.filter(c_name=course.c_name).aggregate(Avg('s_ratings'))['s_ratings__avg']
            rating_count = RatingReview.objects.filter(c_name=course.c_name).count()
            if avg_rating is None:
                avg_rating = '0'  # Convert to string if None
            else:
                avg_rating = str(avg_rating)  # Convert to string
            courses_with_avg_rating.append((course.c_name, course.c_tfees, course.c_eligibility, course.c_description, course.c_rstream, course.c_type, course.c_img, course.c_code, avg_rating, rating_count))

        # Sort courses based on average rating in descending order
        courses_with_avg_rating.sort(key=lambda x: x[9], reverse=True)

        # Get the top 5 courses with highest average ratings
        top_5_courses_with_avg = courses_with_avg_rating[:5]
        print(top_5_courses_with_avg)

        # Fetch top 5 combinations of percentage, stream, and budget
        top_combinations = userinput.objects.values('percentage', 'stream', 'budget').annotate(count=Count('id')).order_by('-count')[:5]

        # Filter recommended courses based on top combinations
        recommended_courses = []
        for combination in top_combinations:
            percentage = combination['percentage']
            stream = combination['stream']
            budget = combination['budget']

            # Retrieve user input from the saved instance
            user_input = userinput.objects.filter(percentage=percentage, stream=stream, budget=budget).first()

            # Ensure user input exists before filtering courses
            if user_input:
                courses_queryset = courses.objects.filter(c_eligibility=user_input.percentage, c_rstream=user_input.stream, c_tfees=user_input.budget)
                recommended_courses.extend(courses_queryset)

        # Pass data to the template
        return render(request, "home.html", {'Courses': top_5_courses_with_avg, 'Coursess': recommended_courses})

def transfer_courses(request):
    if 'filtered_courses' in request.session:
        filtered_courses = request.session.pop('filtered_courses')
        return render(request, 'Recommender.html', {'filtered_courses': filtered_courses})
    else:
        return render(request, 'Recommender.html')

def coursedetails(request, course_id):
    # Retrieve the course object using the course_id
    course = courses.objects.get(id=course_id)
    # Render the course detail template with the course object
    return render(request, 'coursedetails.html', {'course2': course})