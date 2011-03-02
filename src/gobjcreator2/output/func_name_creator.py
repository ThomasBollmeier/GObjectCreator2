class FuncNameCreator(object):
    
    def __init__(self):
        
        self._intf_funcs = {}
        
    def create_impl_func_name(self, method_name, interface_name=""):
        
        if not interface_name:
            return method_name + "_im"
        else:
            if method_name not in self._intf_funcs:
                res = method_name + "_im"
                self._intf_funcs[method_name] = {interface_name: res}
                return res
            else:
                func_names = self._intf_funcs[method_name]
                if interface_name in func_names:
                    return func_names[interface_name]
                else:
                    res = method_name + "_%d_im" % len(func_names)
                    func_names[interface_name] = res
                    return res 
        