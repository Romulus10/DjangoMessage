from model_bakery import baker


def test_message():
    m = baker.make('clinic_messages.Message')
    assert str(m) == m.subject
