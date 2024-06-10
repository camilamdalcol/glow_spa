from flask import Blueprint, render_template, redirect, url_for, flash
from forms.contact_form import ContactForm
from models.contact_message import ContactMessage

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@main_bp.route('/index.html')
def index():
    return render_template('index.html')

@main_bp.route('/about.html')
def about():
    return render_template('about.html')

@main_bp.route('/services.html')
def services():
    return render_template('services.html')

@main_bp.route('/testimonial.html')
def testimonial():
    return render_template('testimonial.html')

@main_bp.route('/contact.html', methods=['GET', 'POST'])
def contact():
    from app import db  # Importe db dentro da rota
    form = ContactForm()
    if form.validate_on_submit():
        try:
            # Obter dados do formulário
            name = form.name.data
            email = form.email.data
            phone = form.phone.data
            message = form.message.data

            # Criar uma nova instância de ContactMessage com os dados fornecidos
            new_message = ContactMessage(name=name, email=email, phone=phone, message=message)

            # Adicionar a nova mensagem ao banco de dados
            db.session.add(new_message)
            db.session.commit()

            # Enviar mensagem de sucesso
            flash("Message sent successfully!", "success")
            
            # Redirecionar de volta para a página de contato
            return redirect(url_for("main.contact"))
        except Exception as e:
            flash('An error occurred while sending the message. Please try again later.', 'error')
            db.session.rollback()  # Rollback no caso de erro

    return render_template('contact.html', form=form)
