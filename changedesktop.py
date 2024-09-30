import i3ipc

def get_next_workspace(current, workspaces):
    # Ordena los workspaces por nombre numérico
    ordered_workspaces = sorted(workspaces, key=lambda ws: int(ws.name))
    
    # Busca el siguiente workspace
    for i, ws in enumerate(ordered_workspaces):
        if ws.name == current:
            # Devuelve el siguiente workspace o el primero si estamos en el último
            return ordered_workspaces[(i + 1) % len(ordered_workspaces)].name

def main():
    i3 = i3ipc.Connection()
    
    # Obtén el workspace actual
    current_workspace = i3.get_tree().find_focused().workspace().name
    
    # Obtén todos los workspaces disponibles
    workspaces = i3.get_workspaces()
    
    # Determina el siguiente workspace
    next_workspace = get_next_workspace(current_workspace, workspaces)
    
    # Cambia al siguiente workspace
    i3.command(f'workspace {next_workspace}')

if __name__ == '__main__':
    main()
