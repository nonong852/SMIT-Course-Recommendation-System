from django.shortcuts import render, redirect
from django.http import HttpResponse
from RandR.models import RatingReview
from home.models import courses

def RandR(request):
    return render(request, 'RandR.html')

def look_up(request):
    if request.method == 'POST':
        registration_number = request.POST.get('s_reg')
        
        if registration_number:
            if registration_number[4:7]=="214":
                course_code_str="214"
            elif registration_number[4:7]=="212":
                course_code_str="212"
            elif registration_number[4:7]=="213":
                course_code_str="213"
            else:
                course_code_str = registration_number[4:6]  # Assuming course code is at position 4 and 5 in the registration number
            print(course_code_str)
            if course_code_str == "00":
                course_code_str = "1"
                print(course_code_str)
                try:
                    course_code = int(course_code_str)
                    course_list = courses.objects.filter(c_code=course_code)
                    
                    # Collecting all course names
                    course_names = [course.c_name for course in course_list]
                    
                    return render(request, 'RandR.html', {'s_reg': registration_number, 'c_names': course_names})
                except courses.DoesNotExist:
                    return render(request, 'RandR.html', {'s_reg': registration_number, 'c_names': 'Course not found'})
                except ValueError:
                    return render(request, 'RandR.html', {'s_reg': registration_number, 'c_names': 'Invalid registration number format'})
            elif course_code_str == "21":
                course_code_str = "21"
                print(course_code_str)
                try:
                    course_code = int(course_code_str)
                    course_list = courses.objects.filter(c_code=course_code)
                    
                    # Collecting all course names
                    course_names = [course.c_name for course in course_list]
                    
                    return render(request, 'RandR.html', {'s_reg': registration_number, 'c_names': course_names})
                except courses.DoesNotExist:
                    return render(request, 'RandR.html', {'s_reg': registration_number, 'c_names': 'Course not found'})
                except ValueError:
                    return render(request, 'RandR.html', {'s_reg': registration_number, 'c_names': 'Invalid registration number format'})
            elif course_code_str == "27":
                course_code_str = "27"
                print(course_code_str)
                try:
                    course_code = int(course_code_str)
                    course_list = courses.objects.filter(c_code=course_code)
                    
                    # Collecting all course names
                    course_names = [course.c_name for course in course_list]
                    
                    return render(request, 'RandR.html', {'s_reg': registration_number, 'c_name': course_names})
                except courses.DoesNotExist:
                    return render(request, 'RandR.html', {'s_reg': registration_number, 'c_name': 'Course not found'})
                except ValueError:
                    return render(request, 'RandR.html', {'s_reg': registration_number, 'c_name': 'Invalid registration number format'})
            elif course_code_str == "25":
                course_code_str = "25"
                print(course_code_str)
                try:
                    course_code = int(course_code_str)
                    course_list = courses.objects.filter(c_code=course_code)
                    
                    # Collecting all course names
                    course_names = [course.c_name for course in course_list]
                    
                    return render(request, 'RandR.html', {'s_reg': registration_number, 'c_name': course_names})
                except courses.DoesNotExist:
                    return render(request, 'RandR.html', {'s_reg': registration_number, 'c_name': 'Course not found'})
                except ValueError:
                    return render(request, 'RandR.html', {'s_reg': registration_number, 'c_name': 'Invalid registration number format'})
            elif course_code_str == "26":
                course_code_str = "26"
                print(course_code_str)
                try:
                    course_code = int(course_code_str)
                    course_list = courses.objects.filter(c_code=course_code)
                    
                    # Collecting all course names
                    course_names = [course.c_name for course in course_list]
                    
                    return render(request, 'RandR.html', {'s_reg': registration_number, 'c_name': course_names})
                except courses.DoesNotExist:
                    return render(request, 'RandR.html', {'s_reg': registration_number, 'c_name': 'Course not found'})
                except ValueError:
                    return render(request, 'RandR.html', {'s_reg': registration_number, 'c_name': 'Invalid registration number format'})
            elif course_code_str == "28":
                course_code_str = "28"
                print(course_code_str)
                try:
                    course_code = int(course_code_str)
                    course_list = courses.objects.filter(c_code=course_code)
                    
                    # Collecting all course names
                    course_names = [course.c_name for course in course_list]
                    
                    return render(request, 'RandR.html', {'s_reg': registration_number, 'c_name': course_names})
                except courses.DoesNotExist:
                    return render(request, 'RandR.html', {'s_reg': registration_number, 'c_name': 'Course not found'})
                except ValueError:
                    return render(request, 'RandR.html', {'s_reg': registration_number, 'c_name': 'Invalid registration number format'})
            elif course_code_str == "214":
                print(course_code_str)
                try:
                    course_code = int(course_code_str)
                    course_list = courses.objects.filter(c_code=course_code)
                    
                    # Collecting all course names
                    course_names = [course.c_name for course in course_list]
                    
                    return render(request, 'RandR.html', {'s_reg': registration_number, 'c_name': course_names})
                except courses.DoesNotExist:
                    return render(request, 'RandR.html', {'s_reg': registration_number, 'c_name': 'Course not found'})
                except ValueError:
                    return render(request, 'RandR.html', {'s_reg': registration_number, 'c_name': 'Invalid registration number format'})
            elif course_code_str == "212":
                print(course_code_str)
                try:
                    course_code = int(course_code_str)
                    course_list = courses.objects.filter(c_code=course_code)
                    
                    # Collecting all course names
                    course_names = [course.c_name for course in course_list]
                    
                    return render(request, 'RandR.html', {'s_reg': registration_number, 'c_name': course_names})
                except courses.DoesNotExist:
                    return render(request, 'RandR.html', {'s_reg': registration_number, 'c_name': 'Course not found'})
                except ValueError:
                    return render(request, 'RandR.html', {'s_reg': registration_number, 'c_name': 'Invalid registration number format'})
            elif course_code_str == "213":
                print(course_code_str)
                try:
                    course_code = int(course_code_str)
                    course_list = courses.objects.filter(c_code=course_code)
                    
                    # Collecting all course names
                    course_names = [course.c_name for course in course_list]
                    
                    return render(request, 'RandR.html', {'s_reg': registration_number, 'c_name': course_names})
                except courses.DoesNotExist:
                    return render(request, 'RandR.html', {'s_reg': registration_number, 'c_name': 'Course not found'})
                except ValueError:
                    return render(request, 'RandR.html', {'s_reg': registration_number, 'c_name': 'Invalid registration number format'})
            else:
                try:
                    course_code = int(course_code_str)
                    course = courses.objects.get(c_code=course_code)
                    return render(request, 'RandR.html', {'s_reg': registration_number, 'c_name': course.c_name})
                except courses.DoesNotExist:
                    return render(request, 'RandR.html', {'s_reg': registration_number, 'c_name': 'Course not found'})
                except ValueError:
                    return render(request, 'RandR.html', {'s_reg': registration_number, 'c_name': 'Invalid registration number format'})
        else:
            return render(request, 'RandR.html', {'c_name': 'Registration number is empty'})
    else:
        return redirect('RandR')  # Redirect to RandR page if it's not a POST request

def submit_review(request):
    if request.method == 'POST':
        registration_number = request.POST.get('s_reg')
        course_name = request.POST.get('c_name')
        rating = request.POST.get('s_rating')
        review = request.POST.get('s_review')
        
        if registration_number and course_name and rating and review:
            # Check if a row with the same registration number already exists
            if RatingReview.objects.filter(s_reg=registration_number).exists():
                return render(request, 'RandR.html', {'message': 'Rating and Review already submitted.'})
            else:
                # Save the rating and review to the database
                en = RatingReview(s_reg=registration_number, c_name=course_name, s_ratings=rating, s_reviews=review)
                en.save()
                return render(request, 'RandR.html', {'message': 'Rating and review submitted successfully.'})
        else:
            return render(request, 'RandR.html', {'message': 'Incomplete data. Please fill all fields.'})
    else:
        return render(request, 'RandR.html', {'message': 'Invalid request.'})
