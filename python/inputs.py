import inspect
import traceback

FIELDS_EXECUTION_RITM = [
    'description',
    'origem',
    'ip_router'
]



def prepare_input(inputs: dict):
    inputs_valid = dict(filter(lambda it: it[1] is not None, inputs.items()))
    
    inputs_names = inputs_valid.keys()

    return inputs_valid

teste = {
    'a':'b',
    'x':None,
    'j':231,
    'd':None
}

prepare_input(teste)

def get_all_inputs(params_search: list[str]):
    try:

        module_automation = inspect.getmodule(inspect.stack()[1])
        inputs = {}
        
        for param_search in params_search:
            inputs[param_search] = getattr(module_automation, param_search, None)

        return inputs
    except Exception:
        for param_search in params_search:
            result_error[param_search] = None
        
        print(f"Erro ao tentar ler inputs do motor\n{traceback.format_exc()}")
        result_error = {}
        return result_error 

