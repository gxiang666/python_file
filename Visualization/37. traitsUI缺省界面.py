from traits.api import HasTraits, Str, Int


class ModelManager(HasTraits):
    model_name = Str
    category = Str
    model_file = Str
    model_number = Int

if __name__ == "__main__":
    model = ModelManager()
    model.configure_traits()
