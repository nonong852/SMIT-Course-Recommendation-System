from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.conf import settings
from urllib.parse import urljoin
from home.models import courses  # Import the Course model
from RandR.models import RatingReview
from django.db.models import Avg
# Create your views here.
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from django.db.models import Avg

def calculate_cosine_similarity(query, corpus):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)
    query_vector = tfidf_vectorizer.transform([query])
    cosine_similarities = cosine_similarity(query_vector, tfidf_matrix)
    return cosine_similarities[0]
def Recommender(request):
    filtered_courses = request.GET.getlist('filtered_courses', [])
    print(filtered_courses)
   
     # Modify image paths in filtered_courses
    for course in filtered_courses:
        # Assuming c_img contains the relative path starting from the 'media' directory
        course['c_img'] = urljoin(settings.MEDIA_URL, course['c_img'])

        # Replace '/media/' with '/static/' in the URL
        course['c_img'] = course['c_img'].replace('/media/', '/static/')

    return render(request, 'Recommender.html', {'filtered_courses': filtered_courses})

#def coursedetails(request, course_id):
    # Fetch the course object using the course_id
 #   try:
  #      course = courses.objects.get(pk=course_id)  # Fix the model name to Course
   # except courses.DoesNotExist:
        # Handle the case where the course doesn't exist
    #    return HttpResponse("Course not found.")

    # Pass the course object to the template
   # return render(request, 'coursedetails.html', {'course': course})


def coursedetails(request, course_id):
    try:
        # Fetch the details of the current course
        current_course = courses.objects.get(pk=course_id)
    except courses.DoesNotExist:
        return HttpResponse("Course not found.")

    # Fetch all courses from the database
    all_courses = courses.objects.all()

    # Concatenate features for the current course
    current_course_features = f"{current_course.c_tfees} {current_course.c_eligibility} {current_course.c_rstream} {current_course.c_type}"

    # Calculate cosine similarity between the concatenated features of the current course and other courses
    corpus = [f"{course.c_tfees} {course.c_eligibility} {course.c_rstream} {course.c_type}" for course in all_courses]
    similarities = calculate_cosine_similarity(current_course_features, corpus)

    # Create a list of tuples (course, cosine_similarity)
    courses_with_similarity = [(course, similarity) for course, similarity in zip(all_courses, similarities)]

    # Sort courses based on cosine similarity and exclude the current course
    similar_courses = sorted(courses_with_similarity, key=lambda x: x[1], reverse=True)
    similar_courses = [course for course, _ in similar_courses if course.id != current_course.id]

    # Fetch ratings and reviews for the current course
    ratings_reviews = RatingReview.objects.filter(c_name=current_course.c_name)

    # Calculate average rating
    average = ratings_reviews.aggregate(Avg('s_ratings'))['s_ratings__avg']
    if average is None:
        average = 0
    else:
        average = round(average, 2)

    context = {
        'course': current_course,
        'similar_courses': similar_courses[:5],  # Pass top 5 similar courses to the template
        'ratings_reviews': ratings_reviews,
        'avg_rating': average,
    }

    return render(request, 'coursedetails.html', context)

def filter_courses(request):
    if request.method == 'POST':
        percentage = request.POST.get('percentage')
        stream = request.POST.get('stream')
        coursetype = request.POST.get('courseType')
        if stream =="Humanities" or stream=="Commerce":
            stream="any stream"
        budget = request.POST.get('minamount')
        percentage = int(percentage)
        budget = int(budget)
        print("Form Inputs:", percentage, stream, budget)
        filtered_courses = courses.objects.filter(
            c_eligibility__lte=percentage,
            c_rstream=stream,
            c_type=coursetype,
            c_tfees__lte=budget
        )
        print(filtered_courses.query)
        return render(request, 'Recommender.html',{'course':filtered_courses})