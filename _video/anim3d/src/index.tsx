import React from "react";
import { Composition, registerRoot } from "remotion";
import { PhoDemo, PHO_FRAMES } from "./videos/pho/Pho";
const Root: React.FC = () => <Composition id="PhoDemo" component={PhoDemo} durationInFrames={PHO_FRAMES} fps={30} width={1920} height={1080} />;
registerRoot(Root);
