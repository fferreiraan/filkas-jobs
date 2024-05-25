import inspect
import traceback

def get_all_inputs(params_search: list[str]):
    try:

        module_automation = inspect.getmodule(inspect.stack()[1][0])
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

