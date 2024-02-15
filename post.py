from flask import Blueprint, jsonify, Flask
from models.model_post import Post

post_bp = Blueprint('post', __name__)

@post_bp.route('/', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    serialized_posts = []
    for post in posts:
        serialized_post = {
            'id': post.id,
            'title': post.title,
            'content': post.content,
            # Add other fields as needed
        }
        serialized_posts.append(serialized_post)
    return jsonify(serialized_posts)


@post_bp.route('/<int:id>', methods=['GET'])
def get_posts_by_id(id):
    post = Post.query.get_or_404(id)
    serialized_posts = []
    serialized_post = {
        'id': post.id,
        'title': post.title,
        'content': post.content,
    }
    serialized_posts.append(serialized_post)

    return jsonify(serialized_posts)