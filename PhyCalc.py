#!/usr/bin/env python3
import math
from pathlib import Path
from kivy.app import App
from kivy.uix.button import Button
from kivy.core.text import LabelBase
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window
font_path = str(Path(__file__).parent / "fonts" / "NotoSansCJK-Regular.ttc")
LabelBase.register(name='Chinese', fn_regular=font_path)

class MyApp(App):
    icon = "logo.png"
    def build(self):
        self.title = "PhyCalc"
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        btn1 = Button(text='物理计算', font_name='Chinese')
        btn2 = Button(text='单位换算', font_name='Chinese')
        btn1.bind(on_press=self.btn1_click)
        btn1.bind(on_release=self.btn1_release)
        btn2.bind(on_press=self.btn2_click)
        btn2.bind(on_release=self.btn2_release)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        return layout
    def calculate(self, expression):
        try:
            lines = expression.strip().split("\n")
            namespace = {
                'g': 10,
                'pi': math.pi,
                'sqrt': math.sqrt,
                'cos': math.cos,
                'sin': math.sin,
                'tan': math.tan,
                'log': math.log,
                'Rad': math.radians,
                'Deg': math.degrees,
                '__builtins__': {}
            }
            last_result = None
            for i, line in enumerate(lines):
                line = line.strip()
                if not line:
                    continue
                line_code = line.replace('^', '**')
                is_assignment = '=' in line and not any(op in line for op in ['==', '!=', '<=', '>='])
                if is_assignment:
                    exec(line_code, namespace)
                else:
                    last_result = eval(line_code, {"__builtins__": {}}, namespace)
            last_line = lines[-1].strip()
            is_last_assignment = '=' in last_line and not any(op in last_line for op in ['==', '!=', '<=', '>='])
            if is_last_assignment:
                var_name = last_line.split('=')[0].strip()
                if var_name in namespace:
                    return str(namespace[var_name])
                else:
                    return f"Oops, variable '{var_name}' not found"
            elif last_result is not None:
                return str(last_result)
            elif last_line in namespace:
                return str(namespace[last_line])
            else:
                return "Oops, something wrong happened."
        except ZeroDivisionError:
            return "错误：除数不能为0"
        except NameError as e:
            return f"错误：变量'{e}'未定义"
        except Exception as e:
            return f"Oops, something wrong happened."
    def btn1_click(self, instance):
        # 创建输入框
        content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        text_input = TextInput(hint_text='请输入物理算式', font_name='Chinese', size_hint_y=None, height=50)
        submit_btn = Button(text='计算', font_name='Chinese', size_hint_y=None, height=50)

        # 创建输入弹窗
        input_popup = Popup(
            title='user input',
            title_font='Chinese',
            content=content,
            size_hint=(0.8, 0.4)
        )

        # 绑定提交按钮
        def on_submit(btn):
            user_input = text_input.text
            input_popup.dismiss()
            result_text = self.calculate(user_input)
            result_content = BoxLayout(orientation='vertical', spacing=10, padding=10)
            result_label = Label(text=result_text, font_name='Chinese')
            close_btn = Button(text='关闭', font_name='Chinese', size_hint_y=None, height=50)
            result_content.add_widget(result_label)
            result_content.add_widget(close_btn)
            result_popup = Popup(
                title='calculate result',
                title_font='Chinese',
                content=result_content,
                size_hint=(0.7, 0.3)
            )

            close_btn.bind(on_press=lambda x: result_popup.dismiss())
            result_popup.open()

        submit_btn.bind(on_press=on_submit)
        content.add_widget(text_input)
        content.add_widget(submit_btn)
        input_popup.open()

    def btn1_release(self, instance):
        instance.text = '物理计算'
    def btn2_click(self, instance):
        content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        # 单位类型选择
        type_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=40)
        type_label = Label(text='单位类型:', font_name='Chinese', size_hint_x=0.3)
        type_spinner = Button(text='长度 ▼', font_name='Chinese', size_hint_x=0.7)
        type_layout.add_widget(type_label)
        type_layout.add_widget(type_spinner)

        # 输入区域
        from_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        from_value = TextInput(hint_text='数值', font_name='Chinese', multiline=False)
        from_unit = Button(text='米', font_name='Chinese', size_hint_x=0.3)
        from_layout.add_widget(from_value)
        from_layout.add_widget(from_unit)

        arrow_label = Label(text='↓', font_name='Chinese', size_hint_y=None, height=30)

        # 输出区域
        to_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        to_value = Label(text='结果', font_name='Chinese', size_hint_x=0.7)
        to_unit = Button(text='英尺', font_name='Chinese', size_hint_x=0.3)
        to_layout.add_widget(to_value)
        to_layout.add_widget(to_unit)

        convert_btn = Button(text='转换', font_name='Chinese', size_hint_y=None, height=50)

        content.add_widget(type_layout)
        content.add_widget(from_layout)
        content.add_widget(arrow_label)
        content.add_widget(to_layout)
        content.add_widget(convert_btn)

        popup = Popup(
            title='单位换算',
            title_font='Chinese',
            content=content,
            size_hint=(0.9, 0.7)
        )

        # 转换逻辑
        def convert(btn):
            try:
                value = float(from_value.text)
                from_u = from_unit.text
                to_u = to_unit.text
                type_name = type_spinner.text.replace(' ▼', '')
                result = self.do_convert(type_name, from_u, to_u, value)
                to_value.text = f"{result:.6g}"
            except ValueError:
                to_value.text = "请输入数字"
            except Exception:
                to_value.text = f"错误"

        # 单位切换逻辑（修复作用域问题）
        def cycle_unit(unit_btn):
            # 获取当前类型
            type_name = type_spinner.text.replace(' ▼', '')
            # 调用正确的作用域 self.get_units_list
            units_list = self.get_units_list(type_name)
            current = unit_btn.text
            if current in units_list:
                idx = units_list.index(current)
                next_idx = (idx + 1) % len(units_list)
                unit_btn.text = units_list[next_idx]
            else:
                unit_btn.text = units_list[0]

        # 类型切换逻辑
        types = ['长度', '质量', '时间']
        def cycle_type(btn):
            current = btn.text.replace(' ▼', '')
            idx = types.index(current) if current in types else 0
            next_idx = (idx + 1) % len(types)
            new_type = types[next_idx]
            btn.text = f"{new_type} ▼"
            if new_type == '长度':
                from_unit.text = '米'
                to_unit.text = '英尺'
            elif new_type == '质量':
                from_unit.text = '千克'
                to_unit.text = '磅'
            else:  # 时间
                from_unit.text = '秒'
                to_unit.text = '分钟'
            to_value.text = '结果'
        type_spinner.bind(on_press=cycle_type)
        from_unit.bind(on_press=cycle_unit)
        to_unit.bind(on_press=cycle_unit)
        convert_btn.bind(on_press=convert)
        popup.open()
    def btn2_release(self, instance):
        instance.text = '单位换算'
    def get_units_list(self, type_name):
        units = {
            '长度': ['米', '千米', '厘米', '毫米', '英尺', '英寸', '英里', '码'],
            '质量': ['千克', '克', '毫克', '磅', '盎司', '吨', '斤'],
            '时间': ['秒', '分钟', '小时', '天', '周']
        }
        return units.get(type_name, ['米', '英尺'])

    def do_convert(self, type_name, from_unit, to_unit, value):
        if type_name == '长度':
            to_meter = {
                '米': 1, '千米': 1000, '厘米': 0.01, '毫米': 0.001,
                '英尺': 0.3048, '英寸': 0.0254, '英里': 1609.344, '码': 0.9144
            }
            standard = value * to_meter.get(from_unit, 1)
            from_meter = {
                '米': 1, '千米': 0.001, '厘米': 100, '毫米': 1000,
                '英尺': 1/0.3048, '英寸': 1/0.0254, '英里': 1/1609.344, '码': 1/0.9144
            }
            return standard * from_meter.get(to_unit, 1)
        elif type_name == '质量':
            to_kg = {
                '千克': 1, '克': 0.001, '毫克': 0.000001,
                '磅': 0.453592, '盎司': 0.0283495, '吨': 1000, '斤': 0.5
            }
            standard = value * to_kg.get(from_unit, 1)
            from_kg = {
                '千克': 1, '克': 1000, '毫克': 1000000,
                '磅': 1/0.453592, '盎司': 1/0.0283495, '吨': 0.001, '斤': 2
            }
            return standard * from_kg.get(to_unit, 1)
        else:
            to_sec = {
                '秒': 1, '分钟': 60, '小时': 3600, '天': 86400, '周': 604800
            }
            standard = value * to_sec.get(from_unit, 1)
            from_sec = {
                '秒': 1, '分钟': 1/60, '小时': 1/3600, '天': 1/86400, '周': 1/604800
            }
            return standard * from_sec.get(to_unit, 1)
MyApp().run()
