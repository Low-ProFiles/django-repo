from landing.models import Post, TempUser

new_user = TempUser()
new_user.username = "aquashdw"
new_user.email = "aquashdw@likelion.org"
new_user.save()

target_post = Post.objects.all()[0]
target_post.writer = new_user
target_post.save()

target_post = Post.objects.all()[0]
target_post.writer
target_post.writer.username
target_post.writer.email


liking_user = TempUser.objects.all()[0]
liked_post = Post.objects.all()[0]

liked_post.liked_users.add(liking_user)

new_user = TempUser()
new_user.username = "test_user"
new_user.email = "test@test.com"
new_user.save()

liked_post.liked_users.add(new_user)
liked_post.save()
