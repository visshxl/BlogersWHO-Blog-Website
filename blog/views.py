from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug":"the-mountains",
        "image":"mountain.jpeg",
        "author":"vishal",
        "date":date(2024, 12, 3),
        "title":"Mountain Hiking",
        "excerpt":"""Mountain hiking is an adventurous activity that combines physical endurance 
        with breathtaking views of nature. It offers a chance to explore rugged trails, serene 
        valleys, and majestic peaks. It can be enjoyed solo for introspection or in 
        groups for shared memories.""",
        "content":"""Mountain Hiking
            Mountain hiking is both a physical and mental challenge that brings you closer to nature. It 
            involves trekking through rugged trails, climbing steep slopes, and reaching breathtaking summits. 
            The activity promotes endurance, leg strength, and core stability while refreshing the mind through 
            scenic views and the calming effect of nature.

            Benefits:
            Enhances physical fitness by working various muscle groups.
            Improves mental clarity and reduces stress through connection with nature.
            Strengthens cardiovascular health due to prolonged physical activity.
            Promotes a sense of achievement and boosts self-confidence.
            Tips for Beginners:
            Choose a trail suitable for your fitness level and experience.
            Wear proper hiking boots to prevent injuries.
            Pack essentials such as water, snacks, a map, and a first-aid kit.
            Check the weather and plan your hike accordingly.
            Leave no trace—respect the environment by minimizing your impact.
            """
    },
    {
        "slug":"swim-perks",
        "image":"swimming.jpg",
        "author":"vishal",
        "date":date(2024, 12, 3),
        "title":"Swimming",
        "excerpt":"""Swimming is a low-impact, full-body workout that builds strength, flexibility, 
        and cardiovascular fitness. It’s an excellent activity for all ages, providing both exercise 
        and relaxation. Regular swimming enhances lung capacity, tones muscles, and soothes joints.""",
        "content":"""Swimming is a highly effective, low-impact exercise that engages 
            almost every muscle in the body. It’s suitable for people of all fitness levels, 
            making it a lifelong activity to stay healthy and active.

            Benefits:
            Provides a full-body workout, improving strength, endurance, and flexibility.
            Enhances cardiovascular fitness and lung capacity.
            Supports joint health due to its low-impact nature, making it ideal for injury recovery.
            Reduces stress and promotes mental relaxation through rhythmic movement in water.
            Helps in building water safety and survival skills.
            Tips for Swimming:
            Start with basic strokes like freestyle or backstroke to build confidence.
            Use proper swimming gear like goggles and caps for comfort and efficiency.
            Focus on breathing techniques to maintain rhythm and avoid fatigue.
            Swim in a safe, supervised area and follow all safety protocols.
            Gradually increase your time and intensity in the water to build endurance."""
    },
    {
        "slug":"run-daily",
        "image":"running.webp",
        "author":"vishal",
        "date":date(2024, 12, 3),
        "title":"Running",
        "excerpt":"""Running is a popular cardiovascular exercise that improves heart health and 
        builds stamina. It helps strengthen muscles, enhance mood, and reduce stress. This versatile 
        activity can be done almost anywhere, making it accessible for all fitness levels.""",
        "content":"""Running is a versatile and accessible exercise that suits all fitness levels, 
            from casual joggers to competitive athletes. It is a great way to improve cardiovascular 
            health, boost endurance, and maintain a healthy weight.

            Benefits:
            Strengthens the heart and improves blood circulation.
            Releases endorphins, improving mood and reducing anxiety.
            Helps in weight management and burning calories efficiently.
            Builds leg muscles, enhances bone density, and improves joint health.
            Can be done virtually anywhere—no fancy equipment required!
            Tips for Runners:
            Start slow and gradually increase your distance and pace.
            Wear proper running shoes to avoid discomfort or injuries.
            Warm up before and stretch after your run.
            Stay hydrated and maintain a balanced diet for optimal performance.
            Mix up your routine with interval training or scenic routes to keep it fun."""
    },
    {
        "slug":"the-mountains",
        "image":"mountain.jpeg",
        "author":"vishal",
        "date":date(2024, 4, 24),
        "title":"Mountain Hiking",
        "excerpt":"""Mountain hiking is an adventurous activity that combines physical endurance 
        with breathtaking views of nature. It offers a chance to explore rugged trails, serene 
        valleys, and majestic peaks. It can be enjoyed solo for introspection or in 
        groups for shared memories.""",
        "content":"""Mountain Hiking
            Mountain hiking is both a physical and mental challenge that brings you closer to nature. It 
            involves trekking through rugged trails, climbing steep slopes, and reaching breathtaking summits. 
            The activity promotes endurance, leg strength, and core stability while refreshing the mind through 
            scenic views and the calming effect of nature.

            Benefits:
            Enhances physical fitness by working various muscle groups.
            Improves mental clarity and reduces stress through connection with nature.
            Strengthens cardiovascular health due to prolonged physical activity.
            Promotes a sense of achievement and boosts self-confidence.
            Tips for Beginners:
            Choose a trail suitable for your fitness level and experience.
            Wear proper hiking boots to prevent injuries.
            Pack essentials such as water, snacks, a map, and a first-aid kit.
            Check the weather and plan your hike accordingly.
            Leave no trace—respect the environment by minimizing your impact.
            """
    },
    {
        "slug":"swim-perks",
        "image":"swimming.jpg",
        "author":"vishal",
        "date":date(2024, 10, 4),
        "title":"Swimming",
        "excerpt":"""Swimming is a low-impact, full-body workout that builds strength, flexibility, 
        and cardiovascular fitness. It’s an excellent activity for all ages, providing both exercise 
        and relaxation. Regular swimming enhances lung capacity, tones muscles, and soothes joints.""",
        "content":"""Swimming is a highly effective, low-impact exercise that engages 
            almost every muscle in the body. It’s suitable for people of all fitness levels, 
            making it a lifelong activity to stay healthy and active.

            Benefits:
            Provides a full-body workout, improving strength, endurance, and flexibility.
            Enhances cardiovascular fitness and lung capacity.
            Supports joint health due to its low-impact nature, making it ideal for injury recovery.
            Reduces stress and promotes mental relaxation through rhythmic movement in water.
            Helps in building water safety and survival skills.
            Tips for Swimming:
            Start with basic strokes like freestyle or backstroke to build confidence.
            Use proper swimming gear like goggles and caps for comfort and efficiency.
            Focus on breathing techniques to maintain rhythm and avoid fatigue.
            Swim in a safe, supervised area and follow all safety protocols.
            Gradually increase your time and intensity in the water to build endurance."""
    },
    {
        "slug":"run-daily",
        "image":"running.webp",
        "author":"vishal",
        "date":date(2024, 8, 24),
        "title":"Running",
        "excerpt":"""Running is a popular cardiovascular exercise that improves heart health and 
        builds stamina. It helps strengthen muscles, enhance mood, and reduce stress. This versatile 
        activity can be done almost anywhere, making it accessible for all fitness levels.""",
        "content":"""Running is a versatile and accessible exercise that suits all fitness levels, 
            from casual joggers to competitive athletes. It is a great way to improve cardiovascular 
            health, boost endurance, and maintain a healthy weight.

            Benefits:
            Strengthens the heart and improves blood circulation.
            Releases endorphins, improving mood and reducing anxiety.
            Helps in weight management and burning calories efficiently.
            Builds leg muscles, enhances bone density, and improves joint health.
            Can be done virtually anywhere—no fancy equipment required!
            Tips for Runners:
            Start slow and gradually increase your distance and pace.
            Wear proper running shoes to avoid discomfort or injuries.
            Warm up before and stretch after your run.
            Stay hydrated and maintain a balanced diet for optimal performance.
            Mix up your routine with interval training or scenic routes to keep it fun."""
    }
]

def get_date(post): #helps in sorting
    return post['date']

def starting_page(request):
    sorted_posts=sorted(all_posts, key=get_date) 
    latest_posts= sorted_posts[-3:] # gives the 3 latest posts from the end
    return render(request, "blog/index.html",{
        "posts":latest_posts #passing the stored info to the template
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts":all_posts
    })

def posts_details(request, slug):
    next_post=next(post for post in all_posts if post['slug']==slug)
    return render(request, "blog/post-details.html",{
        "post":next_post
    })