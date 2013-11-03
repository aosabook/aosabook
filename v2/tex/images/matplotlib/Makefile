all: nonaffine_transforms.pdf transform_tree.pdf pixel_snapping.pdf path_simplification.pdf regression.pdf histogram_demo.pdf artists_figure.pdf artists_tree.pdf

nonaffine_transforms.pdf: nonaffine_transforms.py
	python nonaffine_transforms.py

transform_tree.pdf: transform_tree.dot
	dot -Tpdf transform_tree.dot -o transform_tree.pdf

pixel_snapping.pdf: pixel_snapping.py
	python pixel_snapping.py

path_simplification.pdf: path_simplification.py
	python path_simplification.py

regression.pdf: regression.py expected-legend_auto2.png legend_auto2.png failed-diff-legend_auto2.png
	python regression.py

histogram_demo.pdf: histogram_demo.py
	python histogram_demo.py

artists_figure.pdf: artists_figure.py
	python artists_figure.py

artists_tree.pdf: artists_tree.dot
	dot -Tpdf artists_tree.dot -o artists_tree.pdf

