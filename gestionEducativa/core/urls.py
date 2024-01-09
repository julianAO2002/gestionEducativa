from django.urls import path
from . views import HomeView, Pricingview, RegisterView, ProfileView,CoursesView, CourseCreateView, ErrorView,CourseEditView, CourseDeleteView, CourseEnrollmentView, StudentListMarkView, UpdateMarkView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("pricing/", Pricingview.as_view(), name="pricing"),
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", login_required(ProfileView.as_view()), name="profile"),
    path("courses/", CoursesView.as_view(), name="courses"),
    path("courses/create", login_required(CourseCreateView.as_view()), name="courses_create"),
    path("courses/<int:pk>/edit", login_required(CourseEditView.as_view()), name="course_edit"),
    path("courses/<int:pk>/delete", login_required(CourseDeleteView.as_view()), name="course_delete"),
    path("enroll_course/<int:course_id>", CourseEnrollmentView.as_view(), name="enroll_course"),
    path('courses/<int:course_id>', StudentListMarkView.as_view(), name='student_list_mark'),
    path('courses/update_mark/<int:mark_id>', UpdateMarkView.as_view(), name='update_mark'),
    path("error/", login_required(ErrorView.as_view()), name="error"),
]

