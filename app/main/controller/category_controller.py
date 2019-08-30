from flask import request
from flask_restplus import Resource

from ..util.dto import CategoryDto
from ..service.category_service import new_category, get_categories, get_category
from ..util.decorator import token_required

api = CategoryDto.api
_category = CategoryDto.category


@api.route('/')
class getOrPostCategory(Resource):

    @api.doc('list all categories')
    @api.marshal_list_with(_category, envelope='data')
    def get(self):
        return get_categories()

    @api.response(201, 'Category successfully created.')
    @api.doc('create a new category')
    @api.expect(_category, validate=True)
    def post(self):
        data = request.json
        return new_category(data=data)


@api.route('/<id>')
@api.param('id', 'category identifier')
class getCategoryById(Resource):

    @api.response(404, 'Category not found.')
    @api.doc('get a category')
    @api.marshal_list_with(_category)
    def get(self, id):
        category = get_category(id)
        if not category:
            api.abort(404)
        else:
            return category