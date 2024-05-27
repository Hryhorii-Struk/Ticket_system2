

from flask import render_template, redirect, request, url_for
from flask_babel import gettext
from flask_login import login_required

from application import app, flicket_bp
from application.ticket_system.forms.ticket_system_forms import SearchUserForm
from application.ticket_system.models.ticket_system_user import FlicketUser


# view urls.py
@flicket_bp.route(app.config['FLICKET'] + 'urls.py/', methods=['GET', 'POST'])
@flicket_bp.route(app.config['FLICKET'] + 'urls.py/<int:page>/', methods=['GET', 'POST'])
@login_required
def flicket_users(page=1):
    form = SearchUserForm()

    __filter = request.args.get('filter')

    if form.validate_on_submit():
        return redirect(url_for('flicket_bp.flicket_users', filter=form.username.data))

    users = FlicketUser.query

    if __filter:
        filter_1 = FlicketUser.username.ilike('%{}%'.format(__filter))
        filter_2 = FlicketUser.name.ilike('%{}%'.format(__filter))
        filter_3 = FlicketUser.email.ilike('%{}%'.format(__filter))
        users = users.filter(filter_1 | filter_2 | filter_3)
        form.username.data = __filter

    users = users.order_by(FlicketUser.username.asc())
    users = users.paginate(page=page, per_page=app.config['posts_per_page'])

    title = gettext('Users')

    return render_template('ticket_system_users.html',
                           title=title,
                           users=users,
                           form=form)


# view user details
@flicket_bp.route(app.config['FLICKET'] + 'user/<int:user_id>/', methods=['GET', 'POST'])
@login_required
def flicket_user(user_id):
    user = FlicketUser.query.filter_by(id=user_id).one()

    title = gettext('User Details')

    return render_template('ticket_system_user_details.html',
                           title=title,
                           user=user)
