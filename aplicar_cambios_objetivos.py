#!/usr/bin/env python3
"""
Script para aplicar los cambios finales después de ejecutar las migraciones
"""

import os
import sys

def replace_in_file(file_path, old_text, new_text):
    """Reemplaza texto en un archivo"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        content = content.replace(old_text, new_text)
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        
        print(f"✅ Actualizado: {file_path}")
        return True
    except Exception as e:
        print(f"❌ Error actualizando {file_path}: {e}")
        return False

def main():
    print("🔧 Aplicando cambios finales a objetivos...")
    
    # Rutas de archivos
    views_path = "EcoSmart/Planes_app/views.py"
    template_path = "EcoSmart/Planes_app/templates/objetivos.html"
    
    # Cambios en views.py
    print("\n📝 Actualizando views.py...")
    
    # 1. Restaurar select_related
    replace_in_file(views_path, 
        "objetivos_del_plan = Objetivo.objects.filter(plan=plan)",
        "objetivos_del_plan = Objetivo.objects.filter(plan=plan).select_related('creador')")
    
    replace_in_file(views_path,
        "objetivos_del_plan = Objetivo.objects.filter(plan=plan).exclude(estado='completado')",
        "objetivos_del_plan = Objetivo.objects.filter(plan=plan).exclude(estado='completado').select_related('creador')")
    
    # 2. Restaurar asignación de creador
    replace_in_file(views_path,
        """        if form.is_valid():
            objetivo = form.save(commit=False)
            objetivo.plan = plan
            # Establecer monto_actual en 0 por defecto al crear
            if objetivo.monto_actual is None:
                objetivo.monto_actual = 0
            objetivo.save()""",
        """        if form.is_valid():
            objetivo = form.save(commit=False)
            objetivo.plan = plan
            objetivo.creador = request.user
            # Establecer monto_actual en 0 por defecto al crear
            if objetivo.monto_actual is None:
                objetivo.monto_actual = 0
            objetivo.save()""")
    
    # 3. Restaurar verificación de permisos
    replace_in_file(views_path,
        """    # Verificar permisos: solo el admin puede eliminar (temporalmente hasta migración)
    es_admin = (plan.creador == request.user or
                Suscripcion.objects.filter(plan=plan, usuario=request.user, rol='admin').exists())
    
    if not es_admin:
        messages.error(request, 'Solo el administrador puede eliminar objetivos.')
        return redirect('objetivos', plan_id=plan.id)""",
        """    # Verificar permisos: solo el admin o el creador del objetivo pueden eliminarlo
    es_admin = (plan.creador == request.user or
                Suscripcion.objects.filter(plan=plan, usuario=request.user, rol='admin').exists())
    es_creador = objetivo.creador == request.user
    
    if not (es_admin or es_creador):
        messages.error(request, 'Solo el administrador o el creador del objetivo pueden eliminarlo.')
        return redirect('objetivos', plan_id=plan.id)""")
    
    # Cambios en template
    print("\n🎨 Actualizando template...")
    
    # 4. Restaurar mostrar creador
    replace_in_file(template_path,
        """                                <div class="flex items-center gap-4 mt-2 text-sm text-gray-500">
                                    <span class="flex items-center gap-1">
                                        <span class="w-2 h-2 bg-purple-500 rounded-full"></span>
                                        Objetivo de Ahorro
                                    </span>
                                    <span>Meta: ${{ objetivo.monto_necesario|floatformat:2 }}</span>
                                    <span>Actual: ${{ objetivo.monto_actual|floatformat:2 }}</span>
                                </div>""",
        """                                <div class="flex items-center gap-4 mt-2 text-sm text-gray-500">
                                    <span class="flex items-center gap-1">
                                        <span class="w-2 h-2 bg-purple-500 rounded-full"></span>
                                        Creado por: {{ objetivo.creador.username }}
                                    </span>
                                    <span>Meta: ${{ objetivo.monto_necesario|floatformat:2 }}</span>
                                    <span>Actual: ${{ objetivo.monto_actual|floatformat:2 }}</span>
                                </div>""")
    
    # 5. Restaurar verificación de permisos en template
    replace_in_file(template_path,
        "                                {% if es_admin %}",
        "                                {% if es_admin or objetivo.creador == user %}")
    
    print("\n✅ ¡Cambios aplicados exitosamente!")
    print("\n🎯 Funcionalidades implementadas:")
    print("   • Cualquier rol puede crear objetivos")
    print("   • Cada objetivo muestra el nombre del creador")
    print("   • Solo admin y creador pueden eliminar objetivos")
    print("\n🚀 ¡El sistema está listo para usar!")

if __name__ == "__main__":
    main()